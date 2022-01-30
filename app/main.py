import re
import os.path
import configparser
from flask import Flask, render_template

app = Flask(__name__)
config = configparser.ConfigParser()


def getCardsSettings():
    allSections = config.sections()
    regex = re.compile('^card\.[0-9]+$')
    cardSections = [section for section in allSections if re.match(regex, section)]

    cardsContent = []
    for card in cardSections:
        try:
            cardContent = {}
            cardContent['title'] = config[card]['title']
            cardContent['description'] = config[card]['description']
            cardContent['link'] = config[card]['link']
            cardsContent.append(cardContent)
        except:
            continue

    return cardsContent


@app.route('/', methods=['GET'])
def index():
    banner = []
    questionButton = []

    if config.getboolean('banner', 'enable'):
        banner = [config['banner']['title'], config['banner']['content']]

    if config.getboolean('questionbutton', 'enable'):
        questionButton = [config['questionbutton']['title'], config['questionbutton']['content']]
    
    cards = getCardsSettings()

    return render_template('index.html',
                            titlePage = config['main']['titleSite'],
                            header = config['main']['header'],
                            questionButton = questionButton,
                            banner = banner,
                            cards = cards)

if __name__ == '__main__':
    if os.path.isfile('settings.conf'):
        config.read('settings.conf')
        app.run(host = "0.0.0.0", port=5000)
    else:
        print("settings.conf not found")
