
define jose = Character("José")
define juarez = Character("Juarez")


label start:

    play music "Wake up musica.mp3"

    show fundo1
    show jose1
    with dissolve
    jose "Estou muito animado para começar meu primeiro dia como porteiro e fazer tudo corretamente."

    hide jose1
    hide fundo1
    show fundo2
    show juarez1
    with zoomin
    "Nesse mesmo instante, uma pessoa chega na porta do condomínio e toca o interfone."

    hide fundo2
    show fundo1
    hide juarez1
    show jose2
    with fade
    jose "Bom dia! Posso ajudar?"

    hide fundo1
    hide jose2
    show fundo2
    show juarez2
    with moveinleft
    juarez "Bom dia! Vim visitar um primo meu que mora no bloco A."

    hide fundo2
    show fundo1
    hide juarez1
    show jose2
    with fade
    jose "Certo. Qual seu nome e o número do apartamento, por favor?"

    hide fundo1
    hide jose2
    show fundo2
    show juarez2
    with moveinleft
    juarez "Meu nome é Juarez e o apartamento é o 103." ##bug

    hide juarez2
    hide fundo2
    show fundo1
    show jose2
    with fade
    jose "Só um instante, vou interfonar para o apartamento. Qual o nome do morador?"

    hide fundo1
    hide jose3
    show fundo2
    show juarez2
    with moveinleft
    juarez "É Renato. Ah, não precisa! Estou indo fazer uma surpresa de aniversário para ele, pode me liberar."

    hide juarez2
    show fundo1
    show jose3

label minijogo1:

    menu:

        "Interfonar ou deixar entrar?"

        "José deve interfonar primeiro e acabar com a surpresa":

            hide jose3
            show jose5

            "Parabéns! Resposta correta."
            "Sempre se deve interfonar para o morador antes de liberar o acesso."

            jump ligacao
            return

        "José deve liberar a entrada para um desconhecido":

            hide jose3
            show jose4

            "Opa! Resposta errada."
            "José deveria ter interfonado antes e solicitado a liberação do visitante."
            "Tente novamente!"

            show fundo1

            jump minijogo1
            show jose3
            return

label ligacao:

    show jose2
    hide fundo2
    hide jose3
    show fundo1
    jose "Desculpe, senhor, mas preciso que o morador autorize sua entrada."

    hide fundo1
    hide jose3
    show fundo2
    show juarez3
    juarez "Você é novato aqui, né? Os outros porteiros me deixam entrar direto, sempre venho visitar meu primo, todo mundo já me conhece."

    hide fundo2
    hide juarez3
    show fundo1
    show jose2
    jose "São normas do condomínio, senhor. Assim que ele autorizar, já libero sua entrada."

    show jose2
    "José tenta ligar para o apartamento 103, porém depois de várias tentativas, não recebe resposta."
    show jose3

label minijogo2:

    menu:

        "Ninguém atendeu, o que José deve fazer?"

        "Liberar a entrada para Juarez":

            hide jose2
            show jose4

            "Opa! Resposta errada."
            "José deveria ter impedido a entrada já que não houve autorização."
            "Jogue novamente!"

            hide jose2
            show jose5

            jump minijogo2
            return

        "Impedir a entrada sem autorização":

            hide jose2
            show jose5

            "Parabéns! Resposta certa."
            "Sempre que não houver autorização a entrada deve ser proibida."

            jump autorizacao
            return

            hide jose2
            show jose4

        "Ir pessoalmente ao apartamento e bater na porta de Renato":

            hide jose2
            show jose4

            "Opa! Resposta errada."
            "Não se deve deixar a portaria sem vigilância, coisas ruins podem acontecer!"

            hide jose4
            show jose3

            jump minijogo2
            return


label autorizacao:

    hide fundo1
    hide jose2
    show fundo2
    show juarez3
    juarez "Tudo bem, então abre o portão para eu esperar aí dentro, aqui fora tá o maior calorão."

    hide fundo2
    hide juarez3
    show fundo1
    show jose4
    jose "Infelizmente não posso liberar a entrada para não moradores sem autorização."

    hide jose4
    hide fundo1
    show fundo2
    show juarez2
    juarez "Então vou ligar pro meu primo e passar para você ouvir a autorização dele."

    hide juarez2
    hide fundo2
    show fundo1
    show jose3


label minijogo3:

    menu:

        "José deve aceitar a liberação pelo celular de um desconhecido?"

        "Aceitar a ligação do celular de Juarez":

            show jose4

            "Opa! Resposta errada."
            "O porteiro só poderá liberar a entrada se receber a autorização do próprio morador pessoalmente, ou via interfone do condomínio."
            "Jogue novamente!"

            show jose3

            jump minijogo3
            return

            show jose3

        "Não aceitar a ligação":

            show jose5

            "Parabéns! Resposta certa."
            "Ligações de fora do condomínio não podem ser aceitas."

            hide jose5

            jump seguranca
            return


label seguranca:

    hide fundo1
    show fundo2
    hide jose5
    show juarez3
    juarez "Palhaçada... Eu vou falar pro meu primo fazer uma reclamação de você com o síndico daí."

    hide juarez5
    hide fundo2
    show fundo1
    show jose1
    jose "Como queira, senhor. Só estou fazendo o meu trabalho."

    hide jose1
    hide fundo1
    show fundo2
    show juarez4
    "Aparentando chateação, o homem foi embora reclamando."

    hide fundo2
    hide jose1
    show fundo3
    show juarez5
    "Horas depois, José ficou sabendo de um rapaz que estava entrando nos condomínios da redondeza e furtando os apartamentos."
