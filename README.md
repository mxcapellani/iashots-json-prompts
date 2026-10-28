# IAShots JSON Prompts

Versão 1.0.0 — reconstrução fotográfica em JSON estruturado.

Analisa referências para criar instruções fotográficas em inglês, separando a composição de uma fotografia da identidade alternativa fornecida pelo usuário. O núcleo integral está em [.agents/skills/iashots-json-prompts/SKILL.md](.agents/skills/iashots-json-prompts/SKILL.md).

## Contrato preservado
Saída padrão: somente JSON válido com dez chaves exatas, valores descritivos em inglês: Subject, Clothing, Pose, Setting, Camera Settings, Lighting, Effects, Background, Details e Quality. Não há comentários nem chaves adicionais no contrato padrão.

Preservar pose, roupa, cenário, composição e luz, sem copiar traços pessoais da referência de composição. Se não houver identidade separada, usar sujeito neutro, sem características físicas arbitrárias. Excluir textos digitais sobrepostos; texto físico relevante pode permanecer, sem inventar palavras ilegíveis.

## Fluxos
Referência para JSON; composição + identidade; refinamento técnico; auditoria e cena complexa. Os últimos são extensões propostas, não comportamento original empiricamente comprovado. Sem imagem acessível, solicitar envio direto antes de analisar. Um link não prova inspeção visual.

## Uso e instalação
Copiar a pasta `.agents/skills/iashots-json-prompts/` para o diretório aceito pelo host. Ver [instalação](docs/INSTALLATION.md). Pedidos: “Transforme esta foto em JSON” ou “Use A para composição e B para identidade”. A publicação não instala automaticamente a Skill no ChatGPT.

## Modelo-alvo e limites
O nome Nano Banana Pro (Gemini 3 Pro Image) é o alvo declarado na fonte, não compatibilidade atual testada. O JSON organiza instruções e não constitui um payload de API oficial. Recursos de referência, entrada e versão devem ser verificados no gerador utilizado. A análise exige visão e imagens acessíveis; produzir JSON não exige credenciais. Não há geração automática de imagens ou garantia de identidade perfeita.

## Validação
```bash
python -m pip install -r tests/requirements.txt
python tests/validate.py
python tests/test_validator.py
python tests/validate.py --prompt examples/studio-portrait.json
```
Python 3.9+, PyYAML 6.x e jsonschema 4.x. A instalação inicial pode exigir rede; a validação usa apenas arquivos locais. Confere estrutura, dez campos, strings não vazias, duplicatas e exemplo. Não comprova inglês correto, fidelidade visual ou identidade: esses critérios requerem avaliação semântica e geração real.

## Documentação
[Auditoria](docs/AUDIT.md), [comparação](docs/COMPARATIVE-TESTS.md), [schema](schemas/prompt.schema.json) e [exemplo ilustrativo](examples/studio-portrait.json). O anexo foi preservado integralmente no núcleo e em docs; somente a linha vazia antes do frontmatter foi removida.

## Testes e manutenção
Doze casos de aceitação e matriz ponderada estão documentados; execução comportamental permanece pendente. O workflow valida estrutura em push e pull request, sem acessar serviços de geração. Consultar [histórico](CHANGELOG.md) e [contribuições](CONTRIBUTING.md).

MIT, copyright 2026 mxcapellani. Implementação independente sem afiliação aos fornecedores de modelos.
