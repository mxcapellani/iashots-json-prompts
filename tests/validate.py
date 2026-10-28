#!/usr/bin/env python3
"""Contrato estrutural; idioma, identidade e fidelidade requerem avaliação real."""
from pathlib import Path
import argparse
import json
import re
import sys
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
KEYS = ["Subject", "Clothing", "Pose", "Setting", "Camera Settings", "Lighting", "Effects", "Background", "Details", "Quality"]
REQUIRED = [".agents/skills/iashots-json-prompts/SKILL.md", "README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", ".gitignore", "docs/SOURCE_SPECIFICATION.md", "docs/INSTALLATION.md", "docs/AUDIT.md", "docs/COMPARATIVE-TESTS.md", "examples/studio-portrait.json", "schemas/prompt.schema.json", "tests/validate.py", "tests/test_validator.py", "tests/requirements.txt", ".github/workflows/validate.yml"]

def unique(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise ValueError(f"Chave duplicada: {k}")
        out[k] = v
    return out

def load_strict(text):
    def invalid(value):
        raise ValueError(f"Constante JSON inválida: {value}")
    return json.loads(text, object_pairs_hook=unique, parse_constant=invalid)

def validate_prompt(text, root=ROOT):
    try:
        obj = load_strict(text)
        schema = load_strict((Path(root) / "schemas/prompt.schema.json").read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        return [e.message for e in Draft202012Validator(schema).iter_errors(obj)]
    except (ValueError, OSError) as exc:
        return [str(exc)]

class UniqueYaml(yaml.SafeLoader):
    pass

def mapping(loader, node, deep=False):
    return unique([(loader.construct_object(k, deep=deep), loader.construct_object(v, deep=deep)) for k, v in node.value])

UniqueYaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)

def validate(root=ROOT):
    root = Path(root).resolve()
    errors = []
    for rel in REQUIRED:
        p = root / rel
        if not p.is_file() or not p.stat().st_size:
            errors.append(f"Arquivo ausente ou vazio: {rel}")
    skill = root / REQUIRED[0]
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
        try:
            if not match:
                raise ValueError("Frontmatter ausente na primeira linha.")
            data = yaml.load(match.group(1), Loader=UniqueYaml)
            if not isinstance(data, dict) or data.get("name") != "iashots-json-prompts":
                raise ValueError("Nome técnico incorreto.")
            if not isinstance(data.get("description"), str) or not data["description"].strip():
                raise ValueError("Description ausente.")
            for key in KEYS:
                if f'"{key}"' not in text:
                    errors.append(f"Campo não documentado: {key}")
            if len(re.findall(r"^### TEST-\d{3} —", text, re.M)) != 12:
                errors.append("Exigir os doze casos de aceitação fornecidos.")
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"Skill inválida: {exc}")
    schema_file = root / "schemas/prompt.schema.json"
    if schema_file.is_file():
        try:
            schema = load_strict(schema_file.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            if schema.get("required") != KEYS or set(schema.get("properties", {})) != set(KEYS) or schema.get("additionalProperties") is not False:
                errors.append("Schema difere do contrato de dez chaves.")
        except Exception as exc:
            errors.append(f"Schema inválido: {exc}")
    sample = root / "examples/studio-portrait.json"
    if schema_file.is_file() and sample.is_file():
        try:
            errors.extend(validate_prompt(sample.read_text(encoding="utf-8"), root))
        except Exception as exc:
            errors.append(f"Exemplo inválido: {exc}")
    for p in root.rglob("*.md"):
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0]
            if not target or re.match(r"[a-zA-Z][\w+.-]*:", target):
                continue
            dest = (p.parent / target).resolve()
            if not dest.is_relative_to(root) or not dest.exists():
                errors.append(f"Link inválido: {p.relative_to(root)} -> {target}")
    return errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=Path)
    args = parser.parse_args()
    try:
        errors = validate_prompt(args.prompt.read_text(encoding="utf-8")) if args.prompt else validate()
    except OSError as exc:
        errors = [str(exc)]
    for error in errors:
        print(f"ERRO: {error}")
    if not errors:
        print("OK: validação estrutural aprovada; fidelidade e idioma não avaliados automaticamente.")
    sys.exit(bool(errors))
