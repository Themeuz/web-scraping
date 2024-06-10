# Web Scraping – Meerkat Coding, Matheus
 ## Desenvolvendo uma API de raspagem de dados

 ### Ferramentas utilizadas:
- Linguagem Python,
- Requests - biblioteca de leitura de hyper texto (HTTP),
- BeautifulSoup - biblioteca Python para raspagem de dados
- Flask - framework web para aplicações APIs
- Gunicorn - Servidor WSGI para implantar a aplicação Flask


O projeto consiste em ser uma API simples para realizar raspagem de dados de um site. A API foi desenvolvida usando a linguagem Python com as bibliotecas Flask, uma estrutura Web e BS4, uma biblioteca de análise HTML.
A API expõe um endpoit /meerkat que retonra todos os dados encontrados e raspados do site "Bianca.com" com o título, subtítulo, cabeçalhos e paragrafos extraídos.


### Estruturação:

web-scraping/ <br>
│ <br>
├── api/ <br>
│   ├── __init__.py <br>
│   └── scrape.py <br>
├── requirements.txt <br>
└── vercel.json <br>

Todo o código está documentado e muito bem descrito na própria linha do sistema.
Link direto para conectar: http://127.0.0.1:5000/meerkat
