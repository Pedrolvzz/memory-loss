# Depois do Sinal

Um jogo narrativo de mistério e combate por turnos, feito em Python e jogado pelo terminal. Inspirado em Persona e Omori, o projeto explora memória, medo e a dificuldade de pedir ajuda.

## Sinopse

Yu Narukami não veio à aula. No dia seguinte, ninguém reconhecia seu nome.

Apenas você, Makoto e Mitsuri ainda lembram dele. Enquanto as lembranças começam a desaparecer, uma porta surge onde antes havia apenas uma parede na escola.

Você tem **15 dias** para encontrar Narukami. Investigue, converse com seus amigos e descubra o que existe do outro lado antes que você também esqueça por que começou a procurar.

## A história

O desaparecimento de Narukami começa com uma ausência comum: uma carteira vazia na sala de aula. Logo, porém, os professores deixam de reconhecer seu nome, as fotografias mudam e as lembranças que os amigos julgavam seguras começam a falhar.

Você, Makoto e Mitsuri tentam reconstruir seus últimos dias. Cada um conhecia uma parte diferente dele: o amigo que fazia companhia depois da aula, o colega que ajudava nas apresentações, a pessoa que parecia sempre encontrar uma maneira de dizer que estava tudo bem. Conforme a investigação avança, essas lembranças ganham novos significados.

### Os personagens

- **Narukami:** o aluno desaparecido. Para encontrá-lo, será preciso conhecer também o que ele não conseguia contar aos amigos.
- **Makoto:** costuma recorrer ao humor, mas o desaparecimento faz com que revisite uma conversa que deixou pela metade.
- **Mitsuri:** procura preservar o que está desaparecendo. Um áudio e uma fotografia colocam em dúvida até mesmo aquilo de que ela se lembra.
- **O jogador:** participa da investigação e descobre que as próprias lembranças também têm lacunas. Procurar Narukami significa enfrentar perguntas sobre si mesmo.

### Do outro lado da porta

O corredor leva a uma sala em que o tempo parece obedecer a outras regras. Registros antigos se misturam ao presente, mensagens chegam de remetentes impossíveis e uma chamada continua sendo feita. O Regente da Última Chamada controla esse lugar, oferecendo um alívio que torna cada vez mais difícil partir.

A ameaça não se resume ao que pode acontecer dentro da sala. Existe também o medo de voltar para uma vida que continua difícil, de pedir ajuda e de permitir que alguém veja o que você tentou esconder.

### Memória e medo

A história acompanha o esforço de lembrar de alguém sem transformar essa pessoa apenas em seu sofrimento. As conversas revelam afeto, momentos cotidianos e coisas que ficaram por dizer. Os vínculos dão contexto às pistas e mostram por que a busca importa para cada personagem.

O combate é parte dessa jornada, mas não resolve tudo o que ela apresenta. O despertar de Mnemosine se conecta à disposição de encarar lembranças dolorosas, reconhecer os próprios erros e continuar sem a promessa de que tudo voltará a ser como antes.

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
2. Abra um terminal na pasta que contém `main.py`.
3. Execute:

```bash
python main.py
```

No Windows, você também pode usar:

```powershell
py main.py
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

