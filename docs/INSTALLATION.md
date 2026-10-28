# Instalação e atualização

Clonar `https://github.com/mxcapellani/iashots-json-prompts.git` ou baixar o pacote. Manter `.agents/skills/iashots-json-prompts/SKILL.md` no local reconhecido pelo agente. O identificador plural é intencional.

Enviar uma referência de composição real. Se houver referência de identidade, declarar qual é A e qual é B. Sem identidade separada, o prompt permanece neutro; não presumir que a pessoa da composição deve ser reproduzida.

Para validar, instalar dependências do arquivo tests/requirements.txt e executar os comandos do README. Um schema não avalia fidelidade semântica. A entrada do gerador pode exigir adaptação; não enviar esse objeto como payload de API oficial sem documentação específica.

Na atualização, preservar contrato de dez campos, idioma inglês, separação de identidade e tratamento de textos. Registrar versão e repetir testes estruturais e comparativos pertinentes.
