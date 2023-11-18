point = 0
grade = 100
questions = 9
correct = grade / questions


def question_1():
    global point
    global correct

    print('------------------------------------------------------------------------------------------------------------'
          '------------------------------------\n'
          '\nQuestão 1 - O Funcionamento de um Micro-ondas'
          '\n'
          '\nO micro-ondas é um aparelho eletrodoméstico que utiliza ondas eletromagnéticas e foi criado para aquecer e'
          'cozinhar os alimentos com mais \nvelocidade que o forno convencional. Ele funciona a partir de um '
          'dispositivo chamado de magnétron, que irradia micro-ondas para uma ventoinha \nmetálica que as reflete para '
          'acomida, proporcionando o seu aquecimento e cozimento.'
          '\n'
          '\nComo as micro-ondas aquecem os alimentos?'
          '\n'
          '\nA) Pelo atrito causado pela fricção de ar.'
          '\nB) Alterando a composição dos alimentos por radiação ultravioleta.'
          '\nC) Fazendo as moléculas de água que compõe o alimento vibrarem.'
          '\n'
          '\nDigite uma alternativa:')

    answer = input('>> ').upper()

    while answer not in ('A', 'B', 'C'):
        print('\nAlternativa inválida! Digite uma alternativa correta (A, B ou C):')
        answer = input('>> ').upper()

    correct_answer = 'C'

    if answer == correct_answer:
        print('\nParabéns, você acertou!!!'
              '\n'
              '\nQuando as micro-ondas atingem o alimento, as moléculas de água que o compõem vibram, ocasionando uma '
              'fricção que gerará calor, assim o \nalimento é cozido de forma mais simples e rápida.\n')
        point += correct
    else:
        print('\nInfelizmente você errou :('
              '\n'
              '\nQuando as micro-ondas atingem o alimento, as moléculas de água que o compõem vibram, ocasionando uma '
              'fricção que gerará calor, assim o \nalimento é cozido de forma mais simples e rápida.\n'
              '\nPortanto, a alternativa correta era á letra C!\n')


def question_2():
    global point
    global correct

    print('------------------------------------------------------------------------------------------------------------'
          '------------------------------------\n'
          '\nQuestão 2 - As Leis de Newton no Esporte'
          '\n'
          '\nApesar da crença popular de que esportes e ciências são mundos completamente diferentes, os esportes são '
          'laboratórios dinâmicos onde podemos \nver muitos conceitos da física mecânica em prática, principalmente no '
          'que diz respeito às Leis de Newton. Elas estão presentes nos objetos \nque entram e saem de movimento, em '
          'suas trajetórias e nas forças aplicadas sobre eles.'
          '\n'
          '\nDurante um jogo de vôlei os jogadores sentem uma certa pressão sempre que acertam a bola para fazer '
          'alguma jogada. Qual das Leis de Newton \nexplica o porquê do jogador sentir essa pressão?'
          '\n'
          '\nA) Primeira Lei de Newton - Todo corpo continua em seu estado de repouso ou de movimento uniforme em uma '
          'linha reta, a menos que seja forçado \na mudar aquele estado por forças aplicadas sobre ele.'
          '\nB) Segunda Lei de Newton - A mudança de movimento é proporcional à força motora imprimida e é produzida '
          'na direção de linha reta na qual \naquela força é aplicada.'
          '\nC) Terceira Lei de Newton - A toda ação há sempre uma reação oposta e de igual intensidade: as ações '
          'mútuas de dois corpos um sobre o outro \nsão sempre iguais e dirigidas em sentidos opostos.'
          '\n'
          '\nDigite uma alternativa:')

    answer = input('>> ').upper()

    while answer not in ('A', 'B', 'C'):
        print('\nAlternativa inválida! Digite uma alternativa correta (A, B ou C):')
        answer = input('>> ').upper()

    correct_answer = 'C'

    if answer == correct_answer:
        print('\nParabéns, você acertou!!!'
              '\n'
              '\nA Terceira Lei de Newton afirma que para toda ação, há uma reação oposta e de igual intensidade. No '
              'esporte, quando você aplica força a \numa bola, ela aplica uma força igual e oposta em você.\n')
        point += correct
    else:
        print('\nInfelizmente você errou :('
              '\n'
              '\nA Terceira Lei de Newton afirma que para toda ação, há uma reação oposta e de igual intensidade. No '
              'esporte, quando você aplica força a \numa bola, ela aplica uma força igual e oposta em você.\n'
              '\nPortanto, a alternativa correta era á letra C!\n')


def question_3():
    global point
    global correct

    print('------------------------------------------------------------------------------------------------------------'
          '------------------------------------\n'
          '\nQuestão 3- Refração da Luz nas Lentes Ópticas'
          '\n'
          '\nÓculos e lentes de contato corrigem problemas de visão ao utilizar a refração da luz, mostrando como a '
          'física ajuda a melhorar nossa visão.'
          '\n'
          '\nRefração da luz é o fenômeno que consiste na mudança de velocidade de propagação da onda eletromagnética '
          'quando essa atravessa meios ópticos \ndiferentes. A refração pode ou não ser acompanhada de uma mudança na '
          'direção da propagação da luz. Ao passar através das lentes ópticas, a \ndireção de propagação da luz muda.'
          '\n'
          '\nAs lentes podem ser classificadas como divergentes ou convergentes.Em uma lente divergente, quando os '
          'raios de luz incidem paralelos ao eixo \nprincipal, eles sofrem dupla refração e se espalham (esse tipo de '
          'lente é usado para corrigir a miopia). Já na lente convergente, os raios \nde luz incidem paralelos ao eixo '
          'principal e, após sofrerem refração, se concentram em um único ponto (esse tipo de lente é usado para '
          'corrigir \na hipermetropia).'
          '\n'
          '\nComo as lentes corrigem problemas de visão?'
          '\n'
          '\nA) Mudando a cor da luz.'
          '\nB) Mudando a velocidade de propagação da luz.'
          '\nC) Aumentando o brilho das imagens.'
          '\n'
          '\nDigite uma alternativa:')

    answer = input('>> ').upper()

    while answer not in ('A', 'B', 'C'):
        print('\nAlternativa inválida! Digite uma alternativa correta (A, B ou C):')
        answer = input('>> ').upper()

    correct_answer = 'B'

    if answer == correct_answer:
        print('\nParabéns, você acertou!!!'
              '\n'
              '\nAs lentes ópticas utilizam a refração da luz para focalizar os raios de luz na retina, corrigindo '
              'defeitos de visão, como miopia ou \nhipermetropia.\n')
        point += correct
    else:
        print('\nInfelizmente você errou :('
              '\n'
              '\nAs lentes ópticas utilizam a refração da luz para focalizar os raios de luz na retina, corrigindo '
              'defeitos de visão, como miopia ou \nhipermetropia.\n'
              '\n'
              'Portanto, a alternativa correta era á letra B!\n')


def question_4():
    global point
    global correct

    print('------------------------------------------------------------------------------------------------------------'
          '------------------------------------\n'
          '\nQuestão 4 - Ondas Sonoras e Música'
          '\n'
          '\nMúsica é o resultado de uma composição de ondas sonoras (ondas mecânicas). As notas musicais são geradas '
          'pela vibração dos instrumentos \nmusicais e o que as diferencia são as suas frequências: ondas com '
          'frequências diferentes representam notas musicais diferentes, mas toda \nfrequência múltipla de uma nota é '
          'também essa nota. Entretanto, apesar de possuírem a mesma frequência, uma onda de uma mesma nota musical \n'
          'produzida por instrumentos diferentes possui diversas características distintas, dentre elas estão o '
          'timbre, a altura e o volume.'
          '\n'
          '\nO que determina a altura do som em uma música?'
          '\n'
          '\nA) Frequência das ondas sonoras.'
          '\nB) A intensidade do som.'
          '\nC) O formato das ondas sonoras.'
          '\n'
          '\nDigite uma alternativa:')

    answer = input('>> ').upper()

    while answer not in ('A', 'B', 'C'):
        print('\nAlternativa inválida! Digite uma alternativa correta (A, B ou C):')
        answer = input('>> ').upper()

    correct_answer = 'A'

    if answer == correct_answer:
        print('\nParabéns, você acertou!!!'
              '\n'
              '\nA altura do som está associada à sua frequência. Quanto maior a frequência, mais agudo (alto) o som '
              'e quanto menor a frequência, mais grave \n(baixo).\n')
        point += correct
    else:
        print('\nInfelizmente você errou :('
              '\n'
              '\nA altura do som está associada à sua frequência. Quanto maior a frequência, mais agudo (alto) o som '
              'e quanto menor a frequência, mais grave \n(baixo).\n '
              '\nPortanto, a alternativa correta era á letra A!\n')


def question_5():
    global point
    global correct

    print('------------------------------------------------------------------------------------------------------------'
          '------------------------------------\n'
          '\nQuestão 5 - Economia de Combustível em Carros'
          '\n'
          '\nUm dos aspectos mais levado em consideração ao longo da evolução dos modelos de carros é como o seu '
          'formato vai interferir em sua locomoção, \nsempre buscando melhorar sua aerodinâmica.'
          '\n'
          '\nComo a aerodinâmica afeta no gasto de combustível de um veículo?'
          '\n'
          '\nA) Um automóvel com um bom design aerodinâmico sofre mais com a resistência do ar, necessitando de mais '
          'energia para manter a velocidade, \ne por consequência, economizando combustível.'
          '\nB) Um automóvel com um bom design aerodinâmico sofre menos com a resistência do ar, necessitando de menos '
          'energia para manter a velocidade, \ne por consequência, economizando combustível.'
          '\nC) A quantidade de combustível gasta não depende da aerodinâmica do veículo.'
          '\n'
          '\nDigite uma alternativa:')

    answer = input('>> ').upper()

    while answer not in ('A', 'B', 'C'):
        print('\nAlternativa inválida! Digite uma alternativa correta (A, B ou C):')
        answer = input('>> ').upper()

    correct_answer = 'B'

    if answer == correct_answer:
        print('\nParabéns, você acertou!!!'
              '\n'
              '\nO arrasto aerodinâmico se refere à resistência que um corpo enfrenta ao se mover através do ar. '
              'Quando um corpo está se movendo em alta \nvelocidade, o ar cria uma força que se opõe ao seu movimento, '
              'o que dificulta o avanço e exige um maior gasto de energia para manter a \nvelocidade. \n')
        point += correct
    else:
        print('\nInfelizmente você errou :('
              '\n'
              '\nO arrasto aerodinâmico se refere à resistência que um corpo enfrenta ao se mover através do ar. '
              'Quando um corpo está se movendo em alta \nvelocidade, o ar cria uma força que se opõe ao seu movimento, '
              'o que dificulta o avanço e exige um maior gasto de energia para manter a \nvelocidade. Portanto,'
              ' a alternativa correta era á letra B! \n')


def question_6():
    global point
    global correct

    print('------------------------------------------------------------------------------------------------------------'
          '------------------------------------\n'
          '\nQuestão 6 - A Física dos Aparelhos Eletrônicos'
          '\n'
          '\nAtualmente os aparelhos eletrônicos como notebook, tablet e smartphone estão presentes no dia a dia da '
          'maioria das pessoas, tornando-se \nindispensáveis ao estilo de vida moderna. Os modelos mais modernos '
          'possuem tela Touch Screen, ou seja, telas que são sensíveis ao toque.'
          '\n'
          '\nQual dos itens a seguir NÃO é um tipo de tela Touch Screen?'
          '\n'
          '\nA) Tela com sistema capacitivo.'
          '\nB) Tela com sistema infravermelho.'
          '\nC) Tela com sistema eletrotérmico.'
          '\n'
          '\nDigite uma alternativa:')

    answer = input('>> ').upper()

    while answer not in ('A', 'B', 'C'):
        print('\nAlternativa inválida! Digite uma alternativa correta (A, B ou C):')
        answer = input('>> ').upper()

    correct_answer = 'C'

    if answer == correct_answer:
        print('\nParabéns, você acertou!!!'
              '\n'
              '\nOs sistemas capacitivo e infravermelho são tipos de tela Touch Screen.'
              '\n'
              '\nNo sistema capacitivo, uma camada que armazena a carga elétrica é colocada no painel de vidro do '
              'monitor. Quando alguém clica no monitor com \nseu dedo, parte da carga é transferida para essa pessoa, '
              'de modo que a carga na camada capacitiva diminui. Esta diminuição é medida nos \ncircuitos localizados '
              'em cada canto do monitor. Considerando as diferenças relativas de carga em cada canto, o computador '
              'calcula exatamente \nonde ocorreu o toque e então envia esta informação para o software do driver da '
              'tela sensível.\n'
              '\n'
              'Já no sistema infravermelho, as telas usam ondas de luz infravermelha para determinar onde o usuário '
              'coloca o dedo na tela. Uma grade de LEDs \ndispara luz infravermelha em outro conjunto de fotocélulas '
              'de detecção de luz diretamente em frente aos emissores de infravermelho LED. A luz \ninfravermelha é '
              'emitida diretamente na frente da tela para formar uma grade, assemelhando-se a uma teia de aranha '
              'invisível. Ao tocar na tela, \nseu dedo bloqueia os raios de luz infravermelho no ponto de contato. Um '
              'chip de computador é então usado para triangular onde a interrupção \nocorreu.'
              '\n')
        point += correct
    else:
        print('\nInfelizmente você errou :('
              '\n'
              '\nOs sistemas capacitivo e infravermelho são tipos de tela Touch Screen.'
              '\n'
              '\nNo sistema capacitivo, uma camada que armazena a carga elétrica é colocada no painel de vidro do '
              'monitor. Quando alguém clica no monitor com \nseu dedo, parte da carga é transferida para essa pessoa, '
              'de modo que a carga na camada capacitiva diminui. Esta diminuição é medida nos \ncircuitos localizados '
              'em cada canto do monitor. Considerando as diferenças relativas de carga em cada canto, o computador '
              'calcula exatamente \nonde ocorreu o toque e então envia esta informação para o software do driver da '
              'tela sensível.\n'
              '\n'
              'Já no sistema infravermelho, as telas usam ondas de luz infravermelha para determinar onde o usuário '
              'coloca o dedo na tela. Uma grade de LEDs \ndispara luz infravermelha em outro conjunto de fotocélulas '
              'de detecção de luz diretamente em frente aos emissores de infravermelho LED. A luz \ninfravermelha é '
              'emitida diretamente na frente da tela para formar uma grade, assemelhando-se a uma teia de aranha '
              'invisível. Ao tocar na tela, \nseu dedo bloqueia os raios de luz infravermelho no ponto de contato. Um '
              'chip de computador é então usado para triangular onde a interrupção \nocorreu.'
              '\n'
              '\nPortanto a alternativa correta era á letra C! \n')


def question_7():
    global point
    global correct

    print('------------------------------------------------------------------------------------------------------------'
          '------------------------------------\n'
          '\nQuestão 7 - Resfriamento e Condicionamento de Ar'
          '\n'
          '\nSistemas de ar-condicionado usam princípios de termodinâmica para controlar a temperatura de nossos '
          'ambientes, mantendo-nos confortáveis \nem climas quentes ou frios.'
          '\n'
          '\nComo os sistemas de ar-condicionado regulam a temperatura?'
          '\n'
          '\nA) Aquecendo o ar.'
          '\nB) Removendo o oxigênio do ambiente.'
          '\nC) Retirando ar quente do ambiente e devolvendo ar frio.'
          '\n'
          '\nDigite uma alternativa:')

    answer = input('>> ').upper()

    while answer not in ('A', 'B', 'C'):
        print('\nAlternativa inválida! Digite uma alternativa correta (A, B ou C):')
        answer = input('>> ').upper()

    correct_answer = 'C'

    if answer == correct_answer:
        print('\nParabéns, você acertou!!!'
              '\n'
              '\nO funcionamento do ar condicionado se baseia na retirada de ar quente do ambiente e devolução de ar '
              'frio, refrigerado, para o mesmo. Isso \nocorre com base na forma de transferência de calor, denominada '
              'de convecção. A convecção é um processo de troca de calor que acontece através \ndas correntes de '
              'convecção. Essas correntes acontecem por causa das diferenças de densidade entre o ar frio e o ar '
              'quente. O ar quente sendo \nmenos denso sobe, enquanto que, o ar frio (mais denso) desce, formando as '
              'correntes de convecção.\n')
        point += correct
    else:
        print('\nInfelizmente você errou :('
              '\n'
              '\nO funcionamento do ar condicionado se baseia na retirada de ar quente do ambiente e devolução de ar '
              'frio, refrigerado, para o mesmo. Isso \nocorre com base na forma de transferência de calor, denominada '
              'de convecção. A convecção é um processo de troca de calor que acontece através \ndas correntes de '
              'convecção. Essas correntes acontecem por causa das diferenças de densidade entre o ar frio e o ar '
              'quente. O ar quente sendo \nmenos denso sobe, enquanto que, o ar frio (mais denso) desce, formando as '
              'correntes de convecção.'
              '\n'
              '\nPortanto a alternativa correta era á letra C! \n')


def question_8():
    global point
    global correct

    print('------------------------------------------------------------------------------------------------------------'
          '------------------------------------\n'
          '\nQuestão 8 - Forças em Jogo em um Elevador'
          '\n'
          '\nQuando você anda em um elevador, você experimenta as sensações resultantes das forças presentes. Por '
          'exemplo, há momentos em que parece que \nestamos sendo comprimidos contra o chão, enquanto em outros, é '
          'como se o nosso corpo quisesse começar a flutuar.'
          '\n'
          '\nPor que sentimos essa “compressão” quando o elevador sai de seu estado de repouso e começa a subir?'
          '\n'
          '\nA) Porque a gravidade aumenta conforme nos afastamos do solo.'
          '\nB) Porque ao subir o elevador nos deixa mais próximo ao Sol, aumentando a gravidade e consequentemente o '
          'nosso peso.'
          '\nC) Porque a aceleração necessária para fazer o elevador subir, aumenta a força resultante que sentimos.'
          '\n'
          '\nDigite uma alternativa:')

    answer = input('>> ').upper()

    while answer not in ('A', 'B', 'C'):
        print('\nAlternativa inválida! Digite uma alternativa correta (A, B ou C):')
        answer = input('>> ').upper()

    correct_answer = 'C'

    if answer == correct_answer:
        print('\nParabéns, você acertou!!!'
              '\n'
              '\nQuando falamos das forças presentes em um elevador, temos que levar em consideração três forças: '
              'Força Peso (P), Força Normal (N) e Força \nResultante(FR).\n'
              '\n'
              'A força peso surge devido a aceleração da gravidade e pode ser calculada por P = m*g, onde m é a massa '
              'do corpo e g é a aceleração da \ngravidade.\n'
              '\n'
              'A força normal é uma força de reação que surge sempre que um objeto está em contato com uma superfície e'
              'ela é sempre perpendicular à \nsuperfície.\n'
              '\n'
              'E de acordo com a Segunda Lei de Newton, a força resultante pode ser calculada por FR = m*a, onde m é a '
              'massa do corpo e a é a aceleração \ndesenvolvida pelo mesmo. A força resultante sempre ocorre no sentido'
              ' da aceleração.\n'
              '\n'
              'No caso do elevador, as forças peso e normal têm a mesma direção e sentidos opostos: a força peso '
              'sempre aponta para baixo, e neste caso, a \nforça normal aponta para cima. A força resultante '
              'é o resultado da diferença entre essas duas forças, FR = N - P.\n'
              '\n'
              'De acordo com o movimento do elevador podemos sentir diferentes sensações. Assim que o elevador começa '
              'a subir, ele apresenta a aceleração \n(logo, também a força resultante) para cima, o que '
              'leva, consequentemente, à força normal ser maior que a força peso, sendo assim, sentimos \ncomo se '
              'estivéssemos sendo comprimidos contra o chão. Já no momento em que o elevador desacelera, sua '
              'aceleração e força resultante estão \nvoltadas para baixo, deste modo a força peso se torna maior que a '
              'força normal, dando a impressão de que estamos nos desprendendo do chão. \nNa descida, as reações são as'
              ' mesmas, só que em momentos contrários (P>N quando o elevador começa a descida, e N>P quando ele '
              'desacelera).\n'
              '\n'
              'Os momentos onde não parece haver sensação diferente, ocorrem quando o elevador está '
              'parado ou em velocidade constante. Nestes casos não há \naceleração e, por tanto, a força resultante é '
              'nula, ou seja, a força normal é igual a força peso.\n')
        point += correct
    else:
        print('\nInfelizmente você errou :('
              '\n'
              '\nQuando falamos das forças presentes em um elevador, temos que levar em consideração três forças: '
              'Força Peso (P), Força Normal (N) e Força \nResultante(FR).\n'
              '\n'
              'A força peso surge devido a aceleração da gravidade e pode ser calculada por P = m*g, onde m é a massa '
              'do corpo e g é a aceleração da \ngravidade.\n'
              '\n'
              'A força normal é uma força de reação que surge sempre que um objeto está em contato com uma superfície e'
              'ela é sempre perpendicular à \nsuperfície.\n'
              '\n'
              'E de acordo com a Segunda Lei de Newton, a força resultante pode ser calculada por FR = m*a, onde m é a '
              'massa do corpo e a é a aceleração \ndesenvolvida pelo mesmo. A força resultante sempre ocorre no sentido'
              ' da aceleração.\n'
              '\n'
              'No caso do elevador, as forças peso e normal têm a mesma direção e sentidos opostos: a força peso '
              'sempre aponta para baixo, e neste caso, a \nforça normal aponta para cima. A força resultante '
              'é o resultado da diferença entre essas duas forças, FR = N - P.\n'
              '\n'
              'De acordo com o movimento do elevador podemos sentir diferentes sensações. Assim que o elevador começa '
              'a subir, ele apresenta a aceleração \n(logo, também a força resultante) para cima, o que '
              'leva, consequentemente, à força normal ser maior que a força peso, sendo assim, sentimos \ncomo se '
              'estivéssemos sendo comprimidos contra o chão. Já no momento em que o elevador desacelera, sua '
              'aceleração e força resultante estão \nvoltadas para baixo, deste modo a força peso se torna maior que a '
              'força normal, dando a impressão de que estamos nos desprendendo do chão. \nNa descida, as reações são as'
              ' mesmas, só que em momentos contrários (P>N quando o elevador começa a descida, e N>P quando ele '
              'desacelera).\n'
              '\n'
              'Os momentos onde não parece haver sensação diferente, ocorrem quando o elevador está '
              'parado ou em velocidade constante. Nestes casos não há \naceleração e, por tanto, a força resultante é '
              'nula, ou seja, a força normal é igual a força peso.\n'
              '\n'
              'Portanto a alternativa correta era á letra C! \n')


def question_9():
    global point
    global correct

    print('------------------------------------------------------------------------------------------------------------'
          '------------------------------------\n'
          '\nQuestão 9 - Geração de Energia Solar'
          '\n'
          '\nEnergia solar é uma energia renovável proveniente da radiação solar que, através de tecnologias usadas '
          'para o seu aproveitamento, pode ser \nutilizada como fonte direta de energia para aquecimento ou para '
          'produzir energia elétrica. Por ser considerada uma fonte de energia limpa, a \nenergia solar é uma das '
          'fontes alternativas mais promissoras para obtenção energética.'
          '\n'
          '\nQual das alternativas a seguir é uma forma de obter energia elétrica através da energia solar?'
          '\n'
          '\nA) Energia solar nuclear.'
          '\nB) Energia solar geotérmica.'
          '\nC) Energia solar fotovoltaica.'
          '\n'
          '\nDigite uma alternativa:')

    answer = input('>> ').upper()

    while answer not in ('A', 'B', 'C'):
        print('\nAlternativa inválida! Digite uma alternativa correta (A, B ou C):')
        answer = input('>> ').upper()

    correct_answer = 'C'

    if answer == correct_answer:
        print('\nParabéns, você acertou!!!'
              '\n'
              '\nEnergia solar fotovoltaica nada mais é do que a conversão direta da radiação solar em energia'
              'elétrica. Essa conversão é realizada pelas \nchamadas células fotovoltaicas, compostas por material '
              'semicondutor, normalmente o silício. Ao incidir sobre as células, a luz solar provoca a \nmovimentação '
              'dos elétrons do material condutor, transportando-os pelo material até serem captados por um campo '
              'elétrico (formado por uma \ndiferença de potencial existente entre os semicondutores). Dessa forma, '
              'gera-se eletricidade.\n'
              '\nConstituído por painéis, módulos e equipamentos elétricos, o sistema fotovoltaico não exige um '
              'ambiente com alta radiação para funcionar. No \nentanto, a quantidade de energia produzida depende da '
              'densidade das nuvens, ou seja, quanto menos nuvens houver no céu, maior será a produção \nde '
              'eletricidade.')
        point += correct
    else:
        print('\nInfelizmente você errou :('
              '\n'
              '\nEnergia solar fotovoltaica nada mais é do que a conversão direta da radiação solar em energia'
              'elétrica. Essa conversão é realizada pelas \nchamadas células fotovoltaicas, compostas por material '
              'semicondutor, normalmente o silício. Ao incidir sobre as células, a luz solar provoca a \nmovimentação '
              'dos elétrons do material condutor, transportando-os pelo material até serem captados por um campo '
              'elétrico (formado por uma \ndiferença de potencial existente entre os semicondutores). Dessa forma, '
              'gera-se eletricidade.\n'
              '\nConstituído por painéis, módulos e equipamentos elétricos, o sistema fotovoltaico não exige um '
              'ambiente com alta radiação para funcionar. No \nentanto, a quantidade de energia produzida depende da '
              'densidade das nuvens, ou seja, quanto menos nuvens houver no céu, maior será a produção \nde '
              'eletricidade.\n'
              '\n'
              'Portanto a alternativa correta era á letra C! \n')


def main():
    global point

    print('Bem vindo ao Fisicando.IO!!!\n'
          '\nVamos conhecer um pouco mais sobre Física através de uma pequena história.')

    while True:
        print('\nNa cidade de Maringá localizada no Paraná, a vida era uma mistura cativante de fenômenos físicos '
              'e descobertas científicas surpreendentes. \nO personagem principal, Miguel, era um apaixonado por '
              'física, e suas experiências diárias eram cheias de maravilhas. Miguel estava na cozinha \nde sua casa '
              'preparando sua comida quando decidiu esquentar no micro-ondas. Enquanto observava o prato girar e '
              'aquecer, ele pensou nas \nmicro-ondas e como elas faziam para aquecer sua comida. Ficou impressionado '
              'com a maneira como a física estava presente em sua própria casa.\n')

        question_1()

        print('--------------------------------------------------------------------------------------------------------'
              '----------------------------------------\n'
              '\nMais tarde naquele dia, Miguel foi ao parque para relaxar e assistir a um jogo de beisebol. Ele sabia '
              'que o jogo era um exemplo claro das \nleis de Newton em ação. Cada tacada e arremesso eram demonstrações'
              ' vivas das leis da física.\n')

        question_2()

        print('--------------------------------------------------------------------------------------------------------'
              '----------------------------------------\n'
              '\nEnquanto observava o jogo, Miguel notou que precisava de seus óculos para enxergar com clareza. Suas '
              'lentes corrigiam problemas de visão ao \nfocalizar os raios de luz em sua retina. Ele percebeu como a '
              'óptica estava desempenhando um papel fundamental em sua própria experiência visual.\n')

        question_3()

        print('--------------------------------------------------------------------------------------------------------'
              '----------------------------------------\n'
              '\nDepois do jogo, Miguel foi a um concerto ao ar livre. A música o encantou, e ele sabia que a altura '
              'das notas estava relacionada à frequência das ondas sonoras. Ele achava incrível como a física tornava a'
              ' música tão emocionante \ne harmoniosa.\n')

        question_4()

        print('--------------------------------------------------------------------------------------------------------'
              '----------------------------------------\n'
              '\nNo dia seguinte, Miguel decidiu ir a um evento sobre veículos e sustentabilidade. Ele se surpreendeu '
              'ao aprender como a aerodinâmica dos \ncarros afetava a economia de combustível. Ele viu como a física '
              'estava desempenhando um papel vital na criação de carros mais eficientes.\n')

        question_5()

        print('--------------------------------------------------------------------------------------------------------'
              '----------------------------------------\n'
              '\nMiguel passou a tarde em uma exposição de eletrônicos, onde pôde explorar a relação entre '
              'semicondutores e dispositivos eletrônicos modernos. \nEle ficou fascinado com as inovações que a física '
              'possibilitava na eletrônica.\n')

        question_6()

        print('--------------------------------------------------------------------------------------------------------'
              '----------------------------------------\n'
              '\nMais tarde, quando chegou em casa, Miguel estava grato pelo ar-condicionado. Ele sabia que os '
              'sistemas de ar-condicionado regulavam a \ntemperatura, retirando o calor do ambiente e o dissipando do '
              'lado de fora. Ele relaxou e aproveitou o conforto que a física lhe proporcionava.\n')

        question_7()

        print('--------------------------------------------------------------------------------------------------------'
              '----------------------------------------\n'
              '\nNa manhã seguinte, quando foi para o trabalho, Miguel subiu no elevador do edifício. Ele notou o '
              'painel informativo que explicava as forças \nem jogo em um elevador. Ele entendeu por que sentia um peso'
              ' extra quando o elevador acelerava para cima, de acordo com a segunda lei de Newton.\n')

        question_8()

        print('--------------------------------------------------------------------------------------------------------'
              '----------------------------------------\n'
              '\nNo final da semana, Miguel participou de uma palestra sobre energia solar. Ele ficou maravilhado ao '
              'aprender como os painéis solares convertem \na luz do sol em eletricidade por meio do efeito '
              'fotovoltaico, tornando a energia solar uma fonte sustentável e limpa.\n')

        question_9()

        print('--------------------------------------------------------------------------------------------------------'
              '----------------------------------------\n'
              '\nEm Maringá, a vida de Miguel era uma jornada constante de descobertas e maravilhas, onde a física '
              'desempenhava um papel central em todas as \nfacetas de sua vida. Cada experiência diária era uma lição '
              'sobre como a ciência podia tornar o mundo mais fascinante e compreensível.\n')

        print(f'Sua pontuação foi: {round(point)}\n')

        if 90 <= point <= 100:
            print('Parabéns! Você obteve uma nota excelente. Continue assim!')
        elif 80 <= point < 90:
            print('Ótimo trabalho! Sua dedicação está rendendo bons resultados.')
        elif 70 <= point < 80:
            print('Bom desempenho! Continue se esforçando para melhorar ainda mais.')
        elif 60 <= point < 70:
            print('Você está no caminho certo. Identifique as áreas de melhoria e continue se dedicando.')
        elif 50 <= point < 60:
            print('Você está progredindo. Continue focado nos estudos para alcançar melhores resultados.')
        else:
            print('Não desanime! Use essa experiência para aprender e se superar na próxima vez.')

        print('\nDeseja tentar novamente? (S ou N)')
        refresh = input('>> ').upper()

        while refresh not in ('S', 'N'):
            print('\nOpção inválida! Digite uma opção válida (S ou N):')
            refresh = input('>> ').upper()

        if refresh == 'S':
            point = 0
            print('\n--------------------------------------------------------------------------------------------------'
                  '----------------------------------------------')
            continue
        else:
            break


if __name__ == "__main__":
    main()
