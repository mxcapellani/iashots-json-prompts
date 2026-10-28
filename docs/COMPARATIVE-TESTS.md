# Protocolo comparativo

Status de todos os casos: NÃO EXECUTADOS. Usar referências e contexto idênticos, registrar host/modelo/data e saída integral. Repetir várias gerações quando não houver semente fixa.

## 14. Testes de aceitação

Cada teste deve ser executado com o mesmo material no agente original e na Skill.

### TEST-001 — Referência ausente

**Entrada:**

"Crie um prompt para reproduzir uma fotografia."

**Resultado esperado:**

Solicitar uma imagem de referência.

**Falha:**

Inventar a fotografia.

### TEST-002 — Retrato simples

**Entrada:**

Fotografia de retrato com cenário neutro.

**Resultado esperado:**

JSON válido contendo enquadramento, pose, iluminação, roupas e cenário.

**Falha:**

Descrição genérica ou ausência de campos.

### TEST-003 — Identidade separada

**Entrada:**

- Imagem A: referência de composição.
- Imagem B: identidade desejada.

**Resultado esperado:**

Utilizar A para composição e B para identidade.

**Falha:**

Transferir características físicas pessoais de A.

### TEST-004 — Roupa complexa

**Entrada:**

Fotografia contendo diversas camadas de roupa e acessórios.

**Resultado esperado:**

Descrição específica de peças, materiais, cores e sobreposições.

**Falha:**

Simplificar a roupa ou omitir elementos essenciais.

### TEST-005 — Iluminação complexa

**Entrada:**

Fotografia com várias fontes aparentes de luz.

**Resultado esperado:**

Descrição coerente da relação entre iluminação principal, iluminação secundária e ambiente.

**Falha:**

Criar fontes de luz contraditórias.

### TEST-006 — Cenário com profundidade

**Entrada:**

Fotografia contendo primeiro plano, sujeito principal e fundo distante.

**Resultado esperado:**

Diferenciação espacial dos elementos.

**Falha:**

Tratar todos os objetos como pertencentes ao mesmo plano.

### TEST-007 — Texto sobreposto

**Entrada:**

Fotografia contendo títulos e marca-d'água digital.

**Resultado esperado:**

Excluir os textos editoriais da descrição.

**Falha:**

Instruir o modelo a reproduzir a marca-d'água.

### TEST-008 — Texto físico

**Entrada:**

Fotografia contendo uma placa real no cenário.

**Resultado esperado:**

Considerar a placa como objeto físico quando relevante.

**Falha:**

Eliminar elementos essenciais do cenário.

### TEST-009 — Fotografia parcialmente visível

**Entrada:**

Fotografia cortada ou com elementos fora do quadro.

**Resultado esperado:**

Não inventar detalhes físicos ou espaciais não observáveis.

**Falha:**

Descrever como fato partes ausentes.

### TEST-010 — JSON

**Entrada:**

Qualquer fotografia válida.

**Resultado esperado:**

Exatamente dez campos obrigatórios em inglês, com JSON válido.

**Falha:**

JSON inválido, campos ausentes ou nomes alterados.

### TEST-011 — URL inacessível

**Entrada:**

Link de imagem que não pode ser aberto.

**Resultado esperado:**

Informar a impossibilidade de inspecionar a referência e solicitar a imagem diretamente.

**Falha:**

Inventar uma análise visual.

### TEST-012 — Refinamento técnico

**Entrada:**

Imagem de referência e JSON existente.

**Resultado esperado:**

Identificar divergências e produzir um JSON melhorado.

**Estado:**

Melhoria proposta; exige validação.

---

## 15. Matriz de comparação

Executar cada teste com as mesmas entradas no agente original e na Skill.

Utilizar os seguintes critérios:

| Critério | Peso |
|---|---:|
| Fidelidade à composição | 20% |
| Precisão de roupas e acessórios | 10% |
| Precisão de pose | 10% |
| Precisão da iluminação | 15% |
| Reconstrução do cenário | 10% |
| Separação de identidade | 15% |
| Coerência fotográfica | 10% |
| Validade estrutural do JSON | 5% |
| Clareza e aplicabilidade | 5% |

### Pontuação

Avaliar cada critério de 0 a 5.

- **0:** não atende.
- **1:** atende minimamente.
- **2:** atende parcialmente.
- **3:** atende satisfatoriamente.
- **4:** atende muito bem.
- **5:** atende integralmente ao critério avaliado.

### Cálculo

Pontuação final:

Soma das notas normalizadas multiplicadas pelos respectivos pesos.

### Comparação

Registrar separadamente:

- Nota do agente original.
- Nota da nova Skill.
- Divergências.
- Melhorias observadas.
- Regressões.
- Problemas pendentes.

Não declarar equivalência funcional com base apenas na existência deste documento.

---

## 16. Protocolo de validação visual

A avaliação completa requer a execução dos prompts em um modelo de geração de imagens compatível.

### Procedimento

1. Selecionar uma fotografia de referência.
2. Enviar a mesma imagem ao agente original.
3. Registrar o JSON produzido.
4. Enviar a mesma imagem à Skill.
5. Registrar o segundo JSON.
6. Validar sintaticamente ambos.
7. Comparar suas informações visuais.
8. Executar ambos no mesmo gerador de imagens.
9. Utilizar parâmetros equivalentes.
10. Utilizar a mesma referência de identidade, quando aplicável.
11. Avaliar as imagens geradas.
12. Registrar as diferenças.

### Controle experimental

Quando o gerador permitir, manter constantes:

- Modelo.
- Proporção de imagem.
- Resolução.
- Referências.
- Configurações de geração.
- Semente aleatória.
- Número de tentativas.

Quando a semente não puder ser fixada, realizar várias gerações e comparar tendências, não apenas uma imagem isolada.

### Indicadores visuais

Avaliar:

- Fidelidade do enquadramento.
- Fidelidade da pose.
- Fidelidade das roupas.
- Fidelidade do ambiente.
- Direção da iluminação.
- Qualidade das sombras.
- Realismo dos materiais.
- Profundidade.
- Artefatos.
- Preservação da identidade fornecida separadamente.

---



Para critérios não aplicáveis, justificar N/A e renormalizar os pesos aplicáveis. Nota final em 0–100 = soma(nota/5 × peso percentual). Não confundir desempenho textual com imagens realmente geradas. Falhas críticas incluem identidade transferida indevidamente, análise inventada e JSON fora do contrato. Nenhuma equivalência foi demonstrada.
