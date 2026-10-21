# Depois do Sinal

Um jogo narrativo de mistério e combate por turnos, feito em Python e jogado pelo terminal. Inspirado em Persona e Omori, o projeto explora memória, medo e a dificuldade de pedir ajuda.

## Sinopse

Yu Narukami não veio à aula. No dia seguinte, ninguém reconhecia seu nome.

Apenas você, Makoto e Mitsuri ainda lembram dele. Enquanto as lembranças começam a desaparecer, uma porta surge onde antes havia apenas uma parede na escola.

Você tem **15 dias** para encontrar Narukami. Investigue, converse com seus amigos e descubra o que existe do outro lado antes que você também esqueça por que começou a procurar.

## Como jogar

Você escolhe as ações digitando o número indicado no menu e pressionando Enter.

- **Pesquisar na biblioteca:** aumenta o conhecimento e permite descobrir documentos e pistas.
- **Conversar com Makoto ou Mitsuri:** fortalece vínculos e revela lembranças sobre Narukami.
- **Investigar o corredor:** desenvolve a coragem e avança a busca pela sala.
- **Consultar pistas:** mostra as descobertas sem consumir tempo.

Cada atividade de investigação ou conversa consome um período. Os dias são divididos em **tarde e noite**. Depois da noite do dia 15, o prazo termina.

Durante as cenas, pressione **Enter** quando solicitado para continuar a leitura.

### Combate

O confronto é por turnos. Você pode:

| Ação | Efeito |
| --- | --- |
| Atacar | Causa entre 15 e 20 de dano. |
| Recordação — Mnemosine | Causa entre 30 e 40 de dano e consome 10 de energia. |
| Defender | Reduz pela metade o próximo dano recebido e recupera 5 de energia, até o limite de 30. |

O inimigo contra-ataca após uma ação válida, se ainda estiver vivo. Uma escolha inválida ou uma tentativa de usar Recordação sem energia não gasta o turno.

O jogador começa com **100 de vida e 30 de energia**. As barras no terminal acompanham os valores durante a batalha.

## Executar

É necessário ter **Python 3.10 ou superior** instalado. O jogo usa apenas a biblioteca padrão do Python: não é necessário instalar pacotes adicionais.

1. Baixe ou clone este repositório.
2. Abra um terminal na pasta que contém `codigo_corrigido.py`.
3. Execute:

```bash
python codigo_corrigido.py
```

No Windows, você também pode usar:

```powershell
py codigo_corrigido.py
```

Para encerrar antes do final, pressione **Ctrl + C** no terminal.

Use um terminal com suporte a UTF-8 e cores ANSI, como o Windows Terminal ou o terminal integrado do VS Code, para exibir corretamente os acentos, as barras e as cores das falas.

## Sobre o projeto

Este projeto foi desenvolvido como parte do meu aprendizado em Python. A ideia foi praticar programação construindo uma história interativa, com escolhas, passagem do tempo, pistas e combate.

Conceitos utilizados:

- Variáveis, números, strings e valores booleanos.
- Condições com `if`, `elif` e `else`.
- Laços `while` e `for`.
- Listas, `append()`, `in` e `not in`.
- `input()`, f-strings e blocos de texto com aspas triplas.
- `enumerate()` para listar pistas.
- `random.randint()` para sortear danos.
- Códigos ANSI para colorir falas no terminal.

O jogo foi construído com apoio de IA em explicações, revisão de código e desenvolvimento de partes dos diálogos.

## Limitações da versão atual

- O progresso dura apenas a sessão atual: não há salvamento.
- O jogo funciona pelo terminal e não possui interface gráfica ou áudio.
- Os vínculos têm cenas definidas para alguns níveis; continuar conversando depois delas ainda consome tempo e aumenta o vínculo.

## Temas sensíveis

A história aborda isolamento emocional, culpa, medo de abandono e dificuldade de pedir ajuda, além de cenas de tensão e terror psicológico.

## Referências

Persona e Omori são referências criativas. Este é um projeto de estudo de fã, sem vínculo oficial com essas obras. Narukami e o conceito de Persona são referências à série Persona.
