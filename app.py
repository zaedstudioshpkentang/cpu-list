from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://nanoreview.net/en/soc-list/rating"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    cpus = []
    rows = soup.select('table.table-list tbody tr')
    for row in rows:
        processor = row.select_one('td:nth-child(2) a').text.strip()
        brand = row.select_one('td:nth-child(2) .text-gray-small').text.strip()
        rating = row.select_one('td:nth-child(3) .table-list-score-box').text.strip()
        antutu = row.select_one('td:nth-child(4) div').text.strip()
        geekbench = row.select_one('td:nth-child(5) div').text.strip()
        cores = row.select_one('td:nth-child(6)').text.strip()
        clock_speed = row.select_one('td:nth-child(7)').text.strip()
        gpu = row.select_one('td:nth-child(8) div').text.strip()

        cpus.append({
            'processor': processor,
            'brand': brand,
            'rating': rating,
            'antutu': antutu,
            'geekbench': geekbench,
            'cores': cores,
            'clock_speed': clock_speed,
            'gpu': gpu
        })

    return render_template('index.html', cpus=cpus)

if __name__ == "__main__":
    app.run(debug=True)