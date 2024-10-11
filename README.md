Relato do Processo de Criação do Clima 360
Ideia Inicial
O Clima 360 foi concebido como um aplicativo de previsão do tempo, inicialmente focado em fornecer informações detalhadas sobre as condições meteorológicas em tempo real e previsões exclusivas para o Brasil. O objetivo era criar uma solução simples e interativa para que os usuários pudessem obter essas informações de forma rápida, acessível e visualmente atraente.

Ferramentas Utilizadas
Linguagem: Python
API utilizada: OpenWeatherMap
Frameworks: Flask (para desenvolvimento web) e Tkinter (para a interface gráfica local)
IDE: Visual Studio Code
Coleta de Dados Climáticos:

Utilizei a API do OpenWeatherMap para coletar informações climáticas, como temperatura, umidade, velocidade do vento, e previsões do tempo.
Configurei o aplicativo para fazer consultas a partir do nome da cidade inserido pelo usuário e receber as informações climáticas específicas dessa localidade.
Interface de Usuário:

A interface foi projetada para ser simples, com um campo de entrada onde o usuário pode digitar o nome da cidade. Ao clicar em "Enter", os dados são exibidos na tela de maneira clara e organizada.
Adicionei ícones personalizados para representar as condições climáticas (como sol, chuva, nuvens, etc.), e trabalhei para que a interface ficasse visualmente agradável e de fácil uso.
A tela inicial do aplicativo tem a cor de fundo #03396c, onde o nome do app é exibido de maneira centralizada e em destaque. Ao acessar a página de consulta, as informações do clima são exibidas em texto preto para melhor contraste, sem o fundo branco.
Funcionalidades:

O aplicativo permite que o usuário insira o nome da cidade e, ao apertar Enter ou clicar em um botão, ele recebe as informações climáticas dessa cidade.
Ao realizar uma nova consulta, o campo de entrada é automaticamente limpo, permitindo ao usuário fazer outra consulta sem a necessidade de apagar o texto anterior.
O layout foi ajustado para melhorar a legibilidade e exibir as informações de forma mais detalhada e precisa.
Desafios Técnicos:

Um dos principais desafios foi adaptar o código para que ele pudesse ser compatível com o Flask e futuramente ser convertido em um APK para Android.
Enfrentei dificuldades ao tentar configurar as janelas do aplicativo para ter o tamanho ideal e evitar que algumas telas ficassem em branco.
Próximos Passos
Pretendo converter o aplicativo em um APK para que ele possa ser utilizado em dispositivos Android.
Continuar refinando o layout e a usabilidade, buscando uma experiência de usuário cada vez mais intuitiva.
Expandir as funcionalidades para incluir mais detalhes, como previsões por hora e condições específicas, além de ícones mais avançados.
