import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
import random
import time
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def random_delay():
    delay = random.uniform(0.5, 2)
    time.sleep(delay)

def scrape_bianca_home():
    url = 'http://bianca.com'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = {
                'title': soup.title.string if soup.title else 'Sem título encontrado',
                'headings': [h1.text for h1 in soup.find_all('h1')],
                'paragraphs': [p.text.strip() for p in soup.find_all('p')],
                'meta_description': soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else '',
                'last_scraped': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
            return content
        else:
            raise Exception('Erro ao requisitar URL: ' + str(response.status_code))
    except requests.exceptions.RequestException as e:
        raise Exception('Erro ao requisitar URL: ' + str(e))

@app.route('/meerkat', methods=['GET'])
def scrape():
    random_delay()
    data = scrape_bianca_home()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
