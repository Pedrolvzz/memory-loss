import random

matricula = 0
dia = 1
periodo = "tarde"
conhecimento = 1
coragem = 1
vinculo_makoto = 0
vinculo_mitsuri = 0
pistas = []

print("""
=== SINOPSE ===

Yu Narukami não veio à aula.
No dia seguinte, ninguém reconhecia seu nome.

Apenas você, Makoto e Mitsuri ainda lembram dele.
Nas fotografias, seu rosto começa a desaparecer.
Nas conversas, detalhes que pareciam inesquecíveis já não vêm à memória.

Uma porta surge no corredor da escola, onde antes havia apenas uma parede.
Do outro lado, alguém responde à chamada.

Vocês têm 15 dias para encontrar Narukami.
Mas, ao reconstruir os últimos dias dele, percebem
que cada um conhecia uma parte diferente do mesmo amigo.
""")


while True:
    if dia > 15:
        print("""
Você tenta lembrar por que estava investigando aquele corredor.
Makoto... Mitsuri... alguém estava desaparecido?
Você fecha o caderno. As páginas estão em branco.

[FIM - ESQUECIMENTO]
""")
        break


    print(f"======= DIA {dia} — {periodo} =======")
    print(f"Conhecimento: {conhecimento}")
    print(f"Coragem: {coragem}")
    print(f"Vínculo com Makoto: {vinculo_makoto}")
    print(f"Vínculo com Mitsuri: {vinculo_mitsuri}")

    print("""
1 - Pesquisar na Biblioteca 
2 - Conversar com Makoto 
3 - Conversar com Mitsuri 
4 - Investigar Corredor 
5 - Consultar Pistas
""")
    acao = input("Ação: ").lower().strip().replace(" ", "")

    if acao in ("1", "pesquisarnabiblioteca"):
        print(f"Você passou a {periodo} estudando na biblioteca, seu conhecimento aumentou!")
        conhecimento += 1
        print(f"Conhecimento atual: {conhecimento}")

        if conhecimento >= 3:
            pista = "Uma fotografia de 1996 mostra Narukami na mesma aparência de hoje."

            if pista not in pistas:
                print("""
Uma fotografia está datada: 1996.
Narukami aparece na última fileira, com a mesma aparência de hoje.

Você vira o papel.

O nome dele está escrito no verso. Ao passar o dedo,
a tinta ainda fresca deixa uma marca na sua pele.

Você reconhece a letra de Mitsuri.

Abaixo do nome, há outra frase:

\"Se eu esquecer de novo, mostra isso pra mim.\"
""")

                pistas.append(pista)
                print("\n[NOVA PISTA DESCOBERTA]")
                print(pista)

            if "Uma porta identificada como ‘Turma de 1996’ apareceu no corredor. Narukami está preso do outro lado e entregou uma lista de chamada." in pistas and conhecimento >= 4:
                print("Você encontrou o registro de matrícula de Narukami.")

                pista = "O registro confirma: a sala existe desde 1996 e o nome de Narukami foi acrescentado recentemente. Sua matrícula permite solicitar a saída da sala. Matrícula: 2004051"
                if pista not in pistas:

                    pistas.append(pista)
                    print("""
[NOVA PISTA DESCOBERTA!]
O registro confirma: a sala existe desde 1996 e o nome de Narukami foi acrescentado recentemente. Sua matrícula permite solicitar a saída da sala.
O Número da matrícula é: 2004051

Entre os documentos, você encontra o relato de um aluno de 1996.
Ele pediu um lugar onde o dia seguinte nunca chegasse.
A sala apareceu. Desde então, recebe novos alunos e repete o mesmo dia.
Nas fotos antigas, os rostos deles substituem os de quem esteve ali antes.
Narukami não viveu em 1996. Seu rosto foi acrescentado àquela fotografia.

O relato menciona convites enviados por pessoas que nunca os escreveram.
A sala usa a voz, a letra e o número de alguém em quem a pessoa confia.
Foi assim que Narukami recebeu uma mensagem do número de Makoto.

Mais adiante, você encontra uma página com sua própria letra:
"Nós três chegamos até a porta. Ouvimos ele pedir para ficarmos.
Eu tive medo de entrar. A voz ofereceu apagar aquela noite.
Aceitamos. Mitsuri escondeu a foto na biblioteca antes de esquecer."

Você reconhece uma mancha no papel. Lembra de ter derrubado sua caneta.
A lembrança volta incompleta, mas é sua.
A mensagem no verso da foto era uma tentativa de deixar um caminho de volta.

Na última página, há quinze quadrados. Alguns estão riscados.
Abaixo deles: "Depois do décimo quinto dia, o aluno pertence apenas à sala."
Restam exatamente os dias que vocês vinham contando.
""")
            elif "Uma porta identificada como ‘Turma de 1996’ apareceu no corredor. Narukami está preso do outro lado e entregou uma lista de chamada." in pistas:
                print("Os registros usam códigos antigos. Você ainda não consegue interpretá-los.")


        input("\nPressione Enter para continuar...")

        if periodo == "tarde":
            periodo = "noite"
        else:
            periodo = "tarde"
            dia += 1

    elif acao in ("2", "conversarcommakoto"):
        vinculo_makoto += 1

        if vinculo_makoto == 1:
            print("""
\033[34mMakoto: \"Eu mandei mensagem pra ele de novo. Deve estar de saco cheio de mim.\"\033[0m

Ele olha para o celular, mas a tela continua apagada.

\033[34mMakoto: \"Na sexta ele ficou aqui depois da aula. Eu ia embora e ele perguntou se eu podia esperar um pouco.\"\033[0m

\033[34mMakoto: \"Achei que queria ajuda com alguma matéria. Fiz uma piada, falei que cobrava por hora.\"\033[0m

Ele ensaia um sorriso.

\033[34mMakoto: \"Ele riu. Depois disse que não era nada, que eu podia ir.\"\033[0m

\033[34mMakoto: \"Você falou com ele depois disso?\"\033[0m
""")

        print("============================")
        print("Eu sou tu… Tu és eu…")
        print("Entre lembranças que se apagam, um laço se fortalece.")
        print("Teu vínculo com Makoto tornou-se mais forte.")
        print(f"Vínculo com Makoto: {vinculo_makoto}")

        if vinculo_makoto >= 2:
            pista = "Narukami recebeu uma mensagem do número de Makoto, mas ele nega ter enviado"

            if pista not in pistas:
                print("""
\033[34mMakoto: \"Tem uma coisa que eu não contei. Na última noite, ele me mostrou uma mensagem no celular.\"\033[0m
\033[34mMakoto: \"Dizia: venha ao corredor à meia-noite. Quando perguntei quem tinha mandado…\"\033[0m
\033[34mMakoto: \"Ele disse que a mensagem tinha vindo do meu número. Mas eu não mandei nada.\"\033[0m
""")

                pistas.append(pista)
                print("\n[NOVA PISTA DESCOBERTA]")
                print(pista)

        if vinculo_makoto == 3:
            print("""
\033[34mMakoto: “Fiquei pensando no que te contei. Eu nem perguntei por que ele queria que eu esperasse.”\033[0m
\033[34mMakoto: “Não sei se era alguma coisa importante. Talvez não fosse.”\033[0m
\033[34mMakoto: “Mas eu queria ter ficado.”\033[0m
""")
                    
        input("\nPressione Enter para continuar...")

        if periodo == "tarde":
            periodo = "noite"

        else:
            periodo = "tarde"
            dia += 1

    elif acao in ("3", "conversarcommitsuri"):
        vinculo_mitsuri += 1

        if vinculo_mitsuri == 1:
            print("""
\033[95mMitsuri: “Eu odiava apresentar trabalho. Ele ficava no fundo da sala e fazia que sim com a cabeça, mesmo quando eu falava tudo errado.”\033[0m
\033[95mMitsuri: “Depois dizia que eu tinha ido bem. Eu reclamava que ele falava isso de todo mundo.”\033[0m
\033[95mMitsuri: “Ontem eu tinha uma apresentação. Fiquei procurando ele no fundo da sala.”\033[0m
""")

        print("============================")
        print("Eu sou tu… Tu és eu…")
        print("Entre lembranças que se apagam, um laço se fortalece.")
        print("Teu vínculo com Mitsuri tornou-se mais forte.")
        print(f"Vínculo com Mitsuri: {vinculo_mitsuri}")

        if vinculo_mitsuri >= 2:
            pista = "Narukami deixou um bilhete pedindo que procurassem seu nome nos registros antigos da biblioteca."

            if pista not in pistas:
                print("""
\033[95mMitsuri: \"Narukami me entregou um bilhete antes de sumir. Pediu para eu guardar sem ler.\"\033[0m
\033[95mMitsuri: \"Hoje eu abri. Dizia: se eu desaparecer, procure meu nome nos registros antigos da biblioteca.\"\033[0m
\033[95mMitsuri: \"Como alguém pode estar nos registros antigos de uma escola onde acabou de entrar?\"\033[0m
""")

                pistas.append(pista)
                print("\n[NOVA PISTA DESCOBERTA]")
                print(pista)

        if vinculo_mitsuri == 3:
            print("""
\033[95mMitsuri: \"Eu achei um áudio dele. Era pra um trabalho. No final, eu erro uma palavra e a gente começa a rir.\"\033[0m

Ela entrega um dos fones a você.

Você ouve a voz de Mitsuri. Depois, uma pausa.

\033[95mMitsuri: \"Tá ouvindo?\"\033[0m

Há duas risadas, mas só uma voz.

Ela volta alguns segundos e aumenta o volume.
No trecho em que Narukami deveria falar, ouve-se a respiração dele.

\033[95mMitsuri: \"Ontem ainda dava pra entender.\"\033[0m

A gravação termina. Mitsuri continua segurando o celular.

\033[95mMitsuri: \"Eu lembro que ele disse alguma coisa engraçada.\"\033[0m

Ela tenta repetir a frase.

\033[95mMitsuri: \"Me ajuda. Você ouviu esse áudio antes, não ouviu?\"\033[0m
""")

        if vinculo_mitsuri >= 4 and "Uma fotografia de 1996 mostra Narukami na mesma aparência de hoje." in pistas:
            pista = "Mitsuri reconheceu sua letra na fotografia e suspeita que vocês já procuraram Narukami antes."

            if pista not in pistas:
                print("""
\033[95mMitsuri: \"Essa letra é minha.\"\033[0m

Ela vira a foto, procurando alguma coisa.

\033[95mMitsuri: \"Eu escrevo a data em tudo. Por que não coloquei aqui?\"\033[0m

Você aponta para a frase. Mitsuri lê duas vezes.

\033[95mMitsuri: \"Se eu pedi pra você me mostrar… então não é a primeira vez que a gente procura ele.\"\033[0m
""")
                pistas.append(pista)
                print("\n[NOVA PISTA DESCOBERTA]")
                print(pista)

        input("\nPressione Enter para continuar...")

        if periodo == "tarde":
            periodo = "noite"
        else:
            periodo = "tarde"
            dia += 1

    elif acao in ("4", "investigarcorredor"):
        if coragem < 2:
            coragem += 1
            print("""
Você percorre o corredor vazio. Todas as salas estão trancadas.

Toc. Toc. Toc.

Três batidas vêm de dentro da parede.
Você encosta o ouvido. As batidas param.

Uma voz sussurra: \"Não responde.\"

Você se afasta depressa, sem olhar para trás.

Apesar do medo, você sabe que precisa voltar.
Sua coragem aumentou.
""")
            print(f"Coragem atual: {coragem}")

        else:
            pista = "Uma porta identificada como ‘Turma de 1996’ apareceu no corredor. Narukami está preso do outro lado e entregou uma lista de chamada."
            if pista not in pistas:
                print("""
Você retorna ao lugar de onde vieram as batidas.
Desta vez, há uma porta.

Na placa quase apagada, você consegue ler: \"Turma de 1996\".

Você segura a maçaneta. Está gelada.

Do outro lado, uma voz pergunta:
\"Você também recebeu a mensagem?\"

É Narukami. Você tenta abrir a porta, mas ela está trancada.


Você chama por Narukami. Um papel desliza por baixo da porta.

É uma lista de chamada.
A assinatura de Narukami ainda parece úmida.

No rodapé, você lê:
\"Para solicitar a saída de um aluno, apresente seu registro de matrícula.\"

\"O meu está na biblioteca\", Narukami sussurra.

Passos se aproximam do outro lado.

\"Leva a lista. Não deixa ela chamar seu nome.\"

Você guarda o papel.
Quando levanta os olhos, a porta desapareceu.
""")


                pistas.append(pista)
                print("\n[NOVA PISTA DESCOBERTA]")
                print(pista)

            if "O registro confirma: a sala existe desde 1996 e o nome de Narukami foi acrescentado recentemente. Sua matrícula permite solicitar a saída da sala. Matrícula: 2004051" in pistas:
                matricula = input("Digite a matrícula de Narukami: ").strip()

                if matricula == "2004051":
                    print("""
A matrícula faz a fechadura girar. Você encontra Narukami sentado à janela.
Do lado de fora, o mesmo grupo atravessa o pátio, para e atravessa de novo.

Narukami: "Eu sabia que não era o Makoto naquela mensagem.
Mas dizia que eu podia vir sem precisar explicar nada. Eu quis acreditar."

Narukami: "Aqui não tem prova amanhã. Não preciso responder que estou bem.
Eu só queria descansar um pouco. Depois comecei a perder a conta dos dias."

Você pergunta por que ele nunca contou como estava.

Narukami: "Eu tentava. Aí pensava que vocês também tinham problemas.
Quando alguém perguntava, era mais fácil dizer que estava com sono."

Ele olha para a porta aberta, mas não se levanta.

Narukami: "Eu sei que preciso sair… mas tenho medo de voltar
e continuar me sentindo assim."

Você se senta perto dele.

"Você não precisa estar bem para voltar com a gente."

Narukami se levanta. Correntes surgem ao redor dos seus braços.
Uma voz vem da mesa do professor:

"Uma lembrança por outra. Ele sai. Você fica.
Alguém precisa sustentar este dia."

Narukami: "Foi o que ela ofereceu antes. Se ninguém ficar,
ela deixa a gente esquecer. Não aceita de novo."

Você tenta puxar os braços. As correntes não cedem.
O diário se abre numa página escrita com a sua letra.

"Você leu o que fez", diz a voz. "Agora lembre."
""")

                    input("\nPressione Enter para continuar...")

                    print("""
A sala desaparece por um instante.
Você está outra vez diante da porta, naquela primeira noite.
Makoto e Mitsuri estão atrás de você.

Do outro lado, Narukami chama seu nome.
Você segura a maçaneta. Ouve o choro dele. Solta a mão.

"Não consigo", você diz. "Vamos procurar alguém."

Mas o Regente oferece outra saída:
"Ao amanhecer, vocês não precisarão carregar esta noite."

Você se lembra de perguntar se ia doer.
Lembra da resposta. Lembra de aceitar.

Mitsuri se afasta com a fotografia nas mãos.
Você a vê escrever no verso, mas não pergunta o que é.
Só quer que amanheça logo.

A lembrança termina. Narukami continua à sua frente.

"Você já ouviu ele pedir ajuda", diz o Regente.
"Não precisou esquecer para ir embora.
Precisou esquecer para voltar a se achar uma boa pessoa."

Você abre a boca para negar.
Ainda consegue ouvir sua própria voz aceitando o acordo.

Narukami baixa os olhos.

Narukami: "Eu fiquei esperando você voltar."
""")

                    input("\nPressione Enter para continuar...")

                    print("""
Você ensaiou tantas coisas para dizer quando o encontrasse.
Agora nenhuma parece servir.

"Eu ouvi você. Fiquei com medo e fui embora."

Narukami não responde.

"Eu queria encontrar você sem precisar lembrar disso."

O Regente aproxima a caneta do diário.
"Ainda posso apagar. Dessa vez, não haverá bilhete."

Por um instante, você deseja aceitar.
Não ouvir aquela frase outra vez. Não ver o rosto de Narukami.

Você aperta a página entre os dedos.

"Não. Essa lembrança fica comigo."

Você olha para Narukami.

"Você não precisa me perdoar. Mas eu vou abrir essa porta.
Depois, você decide se quer que eu fique."

Ele ergue os olhos. Você espera, mas não pede uma resposta.
""")

                    input("\nPressione Enter para continuar...")

                    print("""
Uma segunda voz ecoa dentro de você.

\"Reconheceste tua própria voz na lembrança que querias apagar.\"

\"Eu sou tu… Tu és eu…\"

\"Se desejas carregá-la e ainda seguir adiante, chama meu nome.\"

A voz vem de dentro de você.
Sua mão ainda treme ao segurar a página. Você não a solta.
Um nome vem à sua boca como uma lembrança.

\"MNEMOSINE!\"
""")

                    input("\nPressione Enter para continuar...")

                    print("""
O Regente tenta riscar a página. A tinta não fixa.

Você chama outra vez. As correntes se partem.
Mnemosine surge atrás de você, com um livro aberto entre as mãos.
Nele, a lembrança permanece inteira.

[SUA PERSONA DESPERTOU]
""")

                    input("\nPressione Enter para continuar...")

                    print("""
Narukami estende a mão. Você avança para ajudá-lo.

Mas ele olha por cima do seu ombro.
Seu braço cai lentamente.

No fundo da sala, uma caneta risca o papel.

\"Há um erro na chamada.\"

Algo se levanta atrás da mesa do professor.
A cabeça roça o teto. Onde deveria haver um rosto,
nomes são escritos e riscados sem parar.

\"Lá fora, vão perguntar se ele já melhorou. Aqui, posso poupar vocês disso.\"

A criatura aponta para Narukami.
Por um instante, você não reconhece o rosto dele.
Narukami diz seu próprio nome em voz alta. Você o repete.

"Ele pode ter medo e ainda querer sair. Abra a porta."

O Regente risca o diário. As correntes se apertam.
Vocês precisarão romper o controle dele para atravessar.

Mnemosine se coloca entre vocês.

A porta se fecha às suas costas.

[O REGENTE DA ÚLTIMA CHAMADA ERGUE A CANETA]
""")

                    input("\nPressione Enter para continuar...")

                    hp_regente = 120
                    hp = 100
                    energia = 30
                    defender = False
                    turno = 1
                    

                    while True:
                        blocos = hp // 10
                        vazios = 10 - blocos
                        blocos_regente = hp_regente // 10
                        vazios_regente = 12 - blocos_regente
                        blocos_energia = energia // 5
                        vazios_energia = 6 - blocos_energia

                        print("==================================================")
                        print(f"\033[31mO REGENTE DA ÚLTIMA CHAMADA · TURNO {turno}\033[0m")
                        print("==================================================")
                        print(f"HP: [{'█' * blocos}{'░' * vazios}] {hp}/100 | Energia: [{'█' * blocos_energia}{'░' * vazios_energia}] {energia}/30 ")
                        print(f"Vida do Regente: [{'█' * blocos_regente}{'░' * vazios_regente}] {hp_regente}/120")
                        print("===========================")
                        print("[1] Atacar")
                        print("[2] Recordação — 10 de energia")
                        print("[3] Defender — recupera 5 de energia")
                        acao1 = input("Ação: ").lower().strip().replace(" ", "")

                        if acao1 in ("1", "atacar"):
                            dano = random.randint(15, 20)
                            print(f"Você avança e golpeia o Regente, causando {dano} de dano!")
                            hp_regente -= dano

                            print("=======================")

                            if hp_regente <= 0:
                                print("O Regente foi derrotado!")
                                break
                            else:
                                dano_regente = random.randint(10, 15)
                                print(f"O Regente risca seu nome no diário. Você sente uma dor súbita e perde {dano_regente} de vida.")
                                hp -= dano_regente

                            turno += 1

                        elif acao1 in ("2", "mnemosine", "recordação", "recordacao"):
                            if energia < 10:
                                print("Você não tem energia suficiente para usar o Mnemosine!")
                                continue
                            else:
                                dano_persona = random.randint(30, 40)
                                print(f"Mnemosine abre seu livro. Lembranças rompem a escuridão e causam {dano_persona} de dano ao Regente!")
                                hp_regente -= dano_persona
                                energia -= 10

                                if hp_regente <= 0:
                                    print("O Regente foi derrotado!")
                                    break
                                else:
                                    dano_regente = random.randint(10, 15)
                                    print(f"O Regente risca seu nome no diário. Você sente uma dor súbita e perde {dano_regente} de vida.")
                                    hp -= dano_regente

                                turno += 1

                        elif acao1 in ("3", "defender"):
                            print("Você se prepara para resistir ao próximo ataque.")
                            energia = min(30, energia + 5)
                            defender = True

                            if defender == True:
                                dano_regente = random.randint(10, 15)
                                dano_defendido = dano_regente // 2

                                hp -= dano_defendido
                                print(f"Você se defende e recebe apenas {dano_defendido} de dano!")
                                defender = False
                                
                                turno += 1

                        else:
                            print("Opção inválida!")
                            continue

                        if hp <= 0:
                            print("Você foi derrotado.")
                            break

                    if hp > 0:
                        input("\nPressione Enter para continuar...")
                        print("\n" * 8)
                        print("""
Você passou tanto tempo tentando não preocupar ninguém
que começou a acreditar que precisava enfrentar tudo sozinho.

Primeiro, deixou de contar as coisas pequenas.
Depois, quando ficaram grandes demais,
já não sabia por onde começar.

As pessoas continuaram perguntando como você estava.
Você continuou respondendo como gostaria de estar.

Até que ser conhecido como alguém forte
virou o seu medo de ser visto em um dia ruim.

Talvez alguém se surpreenda quando você contar.
Talvez diga: “Eu não fazia ideia.”

Isso não torna o que você sentiu menos real.
Só significa que agora essa pessoa sabe.

Você pode deixar que ela saiba.
""")
                        print("\n[FIM]")
                    input("\nPressione Enter para encerrar...")
                    break
                else:
                    print("Matrícula incorreta. Confira o número nas pistas.")
                    continue
            else:
                print("A porta está trancada. Procure o registro de matrícula na biblioteca.")

        input("\nPressione Enter para continuar...")

        if periodo == "tarde":
            periodo = "noite"
        else:
            periodo = "tarde"
            dia += 1

    elif acao in ("5", "consultarpistas"):
        if pistas:
            for posicao, pista in enumerate(pistas, start=1):
                print(f"{posicao}º - {pista}")
        else:
            print("Nenhuma pista encontrada.")

        input("\nPressione Enter para continuar...")
    else:
        print("Opção inválida!")
