import streamlit as st

st.title('Cem bilhões de poemas')

st.write("""
*Os Cem mil bilhões de poemas*, de Raymond Queneau, 1961, é um livro com dez páginas. 
Cada página um poema. Cada poema com 14 versos. 
E cada verso está escrito numa tira, que forma a página. 
Assim o leitor poderá fazer quaisquer combinações entre os poemas e os versos. 
Ou 10 poemas elevados a 14 versos.
Ou 10¹⁴ = 100.000.000.000.000.
100 bilhões de poemas.
""")

from PIL import Image
image = Image.open('queneau.jpg')
st.image(image, caption='Um livro gera 100 bilhões de poemas')

import random
versos = (
    ("O rei dos pampas vira a camisa",
     "Quando tudo termina quando alguém está morrendo",
     "O cavalo do Parthenon fica chateado com seu friso",
     "O velho marinheiro bretão de tabaco pegou a bola",
     "Era às cinco horas em que a marquesa saiu",
     "Do jovem vantajoso, a ninfa estava apaixonada",
     "Ele se abaixa e gostaria de pegar sua mala",
     "Quando um com o outro imediatamente simpatiza",
     "Quando um dia exaltou o aedes prosaico",
     "Mármore para ácido é um deleite"),

    ("Para secar nas pontas dos touros",
    "Quando o trabalhador de mármore polir nossos túmulos",
    "Desde que Lord Elgin negligenciou suas narinas",
    "Para terminar o nariz, excite os arcos",
    "Consumir um chá e depois cupcakes",
    "Snob um pouco nas bordas das bordas fundamentais",
    "Que horda de bandidos cobiçava com certeza",
    "Fazer isso pode ser gêmeos",
    "Desagradar o leigo e os idiotas",
    "Algumas pessoas acima de todos os caracóis"),

    ("O cornedbeef fede do desconto",
    "Seres indecisos falam com você sem franqueza",
    "O turco da época estava vadeando em sua crise",
    "No aparador antigo, ele escolhe sua cereja",
    "O motorista nativo estava esperando na brisa",
    "Uma toga que ele usava que não estava em ordem",
    "Ele se inclina e depois para sua surpresa",
    "A descoberta então que traumatiza",
    "A crítica lúcida vê o que ele está buscando",
    "Na praça, um bombeiro gargareja"),

    ("E os mesmos couros e peles e peles",
    "E tudo passa a significar o fim dos grãos",
    "Ele cantou da mesma forma sim, mas ele cantou falso",
    "Ele só tinha permissão para um e Domingo de Ramos",
    "Ela estava soprando forte nas colinas",
    "Narcisos pegamos ou somos bezerros",
    "Ele não acha tão seco quanto um saco de velhos fayots",
    "Ainda esperamos ser realmente normais",
    "Ele dá à tribo gritos de novos sentidos",
    "Quem sabe se o tubarão está comendo pregado?"),

    ("Ainda me lembro dessa hora requintada",
    "Nós fazemos você se tornar uma mercadoria",
    "O cavalo do Parthenon tremia ao vento",
    "Lembre-se de amigos dessas ilhas da Frísia",
    "Ficamos muito surpresos com esta planície cinza",
    "Quando tiramos fotos dessa torre de Pisa",
    "Ele deplora, deplora tal domínio",
    "E, no entanto, ele era irmão de fingimento",
    "Ambos estão certos, não a multidão rebelde",
    "Do vizinho o Papuan suga o processo"),

    ("Os gaúchos na planície agitavam suas bandeiras",
    "Estamos preparando o caminho para pensamentos sepulcrais",
    "Do cliente de Londres onde as guloseimas brincam",
    "Onde milhares de cordas encalharam",
    "Quando a fúria dos castelos carbonizou",
    "De onde Galileu jogou seus potinhos",
    "Quem gosta de enganar os pobres provinciais",
    "Quem vagabundo se jogou o ouropel",
    "O vulgar insiste em querer belos vermes",
    "O que a horda de ratos não devorou?"),

    ("Estávamos tão frios quanto nus no gelo",
    "Da morte nós enxertamos uma ordem bastarda",
    "Ele estremeceu o pobre homem às margens do Tamisa",
    "Lamentamos um pouco essa pilha de mercadorias",
    "Um barão ousado guarda qualquer imposto especial de consumo",
    "Com uma inscrição etrusca a pedra foi cortada",
    "Ir à cidade grande é um negócio",
    "Mesmo um irmão baixo é a parte indecisa",
    "Ambos estão certos, não a multidão imprecisa",
    "A salada gourmet engole o laburno"),

    ("Quando nos distrair, plante nossos cavaletes",
    "A mariposa mordiscou o tecido ósseo e as cortinas",
    "Quando o gin estraga granizo metralhadora os barcos",
    "Quando você podia ver os arbustos queimando à distância",
    "Quando o bombeiro vem com essas grandes águas",
    "Os gregos e os romanos em vão procuram suas palavras",
    "Ela assusta a Berry como a Morvandiaux",
    "Que pais férteis oferecem berços puros",
    "Não é dado a todos gostar de choques verbais",
    "A criança de olhos azuis gosta de berlingots"),

    ("Da pole para Rosario faz uma boa caminhada",
    "O corajoso pode gritar ah não criou saperlotte",
    "A Grécia de Platão, com certeza, não é estúpida",
    "Secamos o sargo ou o tamboril",
    "Do Ganges ao Malabar, o senhor zozotte inglês",
    "O espírito sopra e respira embaixo da bota",
    "Diante da lama urbana, enrolamos o casaco",
    "O genealogista observa sua garrafa de água quente",
    "O poeta inspirado não é poliglota",
    "O lobo é um amante de galos e caçarolas"),

    ("Aventuras que tivemos que picam lá esfrega",
    "O covarde pode discutir com o rosto pálido",
    "Contamos os espíritos afiados no capô",
    "Sujamos o tubarão que fumamos com uma chalota",
    "Como em Chandernagor, o manant cheira a fezes",
    "O turista em Florença ignora charibotte",
    "Damos um tapa no pirralho que afunda a algema",
    "Coçar o pergaminho se tornará seu cavalo de hobby",
    "Uma língua é suficiente para encher a sua panela",
    "O gato faz um banquete de cabeças de rede"),

    ("Quando você bebe mate, você se torna argentino",
    "Os empreiteiros estão lá para se colocar na turbina",
    "Quando Sócrates morto passou por um duende",
    "Quando você volta ao porto limpando um grão",
    "O coronel coloca um brasão na mão",
    "O treinador chia um pouco de espírito latino",
    "Quando ele vê a lama, procura o esterco",
    "Ele vai querer encontrar o germe adúltero",
    "Mesmo que ele retire o sal do Celtic, é bom",
    "O caminho local se alimenta de excrementos"),

    ("América do Sul seduz ambiguidades",
    "Considerando que, oh leitor, você está sufocando",
    "Sua escultura é ilustre e está no fundo das conchas",
    "Finalmente vendemos tudo lagostas e moscas salgadas",
    "Você não deveria ter abalado os encantos até agora",
    "Os relacionamentos transalpinos são um para um?",
    "Lamentamos no final as cabanas",
    "Irmão, eu te entendo, se você às vezes desbloquear",
    "Bardo que você sempre gosta de mim, solilóquios",
    "Bebíamos pinard o tempo todo"),

    ("Exalte as orelhas barrocas espanholas",
    "Contando o seu leitor de crianças, você se desloca",
    "Transportamos e mármore, detritos e defrock",
    "Pedimos desculpas por não haver baleias ou focas",
    "As Índias têm pingentes suficientes sem isso",
    "Os banqueiros de Avignon trocam os baiques?",
    "Colocamos os malandros mais fétidos",
    "Irmão, vou absolver você, se você me deixar perplexo",
    "Você me surpreende mais do que todos os ventríloquos",
    "Mordiscas pretzels distraem muitas conferências"),

    ("Se o sino estiver silencioso e terlintintin",
    "Tudo, no entanto, deve ter um fim",
    "Se a Europa quer a Europa ou o seu destino",
    "O mamífero é rei, nós somos primos",
    "O escudo do vale ou do ouro dura apenas uma manhã",
    "Beaune e Chianti são o mesmo vinho?",
    "Mas não teríamos visto o metropolitano",
    "A geminação acusa seu destino",
    "O metromane poderoso encarna o adivinho",
    "Mas nada vale a pena grelhar o pedaço de linguiça")
    )

for verse_list in versos:
    st.write(random.choice(verse_list))

st.button("Clique para gerar novo poema")
