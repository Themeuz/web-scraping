# Bibliotecas utilizadas: Flask, BeautifulSoup, Requests
# Utilizei o BS4 por ser mais compatível com pequenos dados para locomoção e linha de código limpa
# Flask para integração com API e para com o web scraping
# Requests para fazer a ponte entre o Python e o hyper text
# Adicionado também a ferramenta random para que possa simular um atraso e evitar bloqueios (em caso de extrações muito pesadas)

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
import random
import time
from datetime import datetime
from flask_cors import CORS

# Configurando o Flask e o CORS para começar com códigos limpos
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT'] = True
CORS(app)

# Função do Random para que possa adicionar um atrao e não comprometa toda a exploração de dados
def random_delay():
    # Gera o atraso esado de 2,5 segundos
    delay = random.uniform(0.5, 2)
    time.sleep(delay)

# Função principal de scraping
def scrape_bianca_home():
    # Nesta aba podemos ver exatamente qual site estamos raspando os dados, no caso é um site fake
    url = 'http://bianca.com'

    # Verifica se o hyper text foi iniciado e compreendido pela ferramenta
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Essa parte extraímos os dados da maneira que desejamos, no caso estamos puxando apenas o que o site pode nos oferecer no momento
            content = {
                'title': soup.title.string if soup.title else 'Sem título encontrado',
                'headings': [h1.text for h1 in soup.find_all('h1')],
                'paragraphs': [p.text.strip() for p in soup.find_all('p')],
                'meta_description': soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else '',
                'last_scraped': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }

            # Os dados extraídos do site são expostos para quem está raspando os dados de forma menos bagunçada exatamente como uma SOPA
            return content
        else:
            raise Exception('Erro ao requisitar URL: ' + str(response.status_code))
    except requests.exceptions.RequestException as e:
        raise Exception('Erro ao requisitar URL: ' + str(e))

# Utilizando as rotas do Flask para acessar os dados via WEB
# Url para conectar = http://127.0.0.1:5000/meerkat
# Explicação: a porta é padrão, o que deixa único seria o trabalho do @app.route que modifica o final para "/meerkat"
@app.route('/meerkat', methods=['GET'])
def scrape():
    random_delay()  # Random delay para atrasar e ter uma dinâmica mais realista
    data = scrape_bianca_home()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
