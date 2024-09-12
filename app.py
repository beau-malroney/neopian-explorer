from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/gallery/')
def gallery():
    images = [
        {'url': '/static/images/anchor_management.png', 'alt': 'Anchor Management', 'link': 'https://www.neopets.com/pirates/anchormanagement.phtml'},
        {'url': '/static/images/apple_bobbing.png', 'alt': 'Apple Bobbing', 'link': 'https://www.neopets.com/halloween/applebobbing.phtml'},
        {'url': '/static/images/daily_puzzle.png', 'alt': 'Daily Puzzle', 'link': 'https://www.jellyneo.net/?go=dailypuzzle'},
        {'url': '/static/images/void_within.gif', 'alt': 'Void Within', 'link': 'https://www.jellyneo.net/?go=the_void_within&id=essence_collection'},
        {'url': '/static/images/daily_interest.png', 'alt': 'Daily Interest', 'link': 'https://www.neopets.com/bank.phtml'},
        {'url': '/static/images/coltzans_shrine.png', 'alt': "Coltzan's Shrine", 'link': 'https://www.neopets.com/desert/shrine.phtml'},
        {'url': '/static/images/deserted_tomb.png', 'alt': 'Deserted Tomb', 'link': 'https://www.neopets.com/worlds/geraptiku/tomb.phtml'},
        {'url': '/static/images/forgotten_shore.png', 'alt': 'Forgotten Shore', 'link': 'https://www.neopets.com/pirates/forgottenshore.phtml'},
        {'url': '/static/images/fruit_machine.png', 'alt': 'Fruit Machine', 'link': 'https://www.neopets.com/desert/fruit/index.phtml'},
        {'url': '/static/images/jelly.png', 'alt': 'Giant Jelly', 'link': 'https://www.neopets.com/jelly/jelly.phtml'},
        {'url': '/static/images/giant_omelette.png', 'alt': 'Giant Omelette', 'link': 'https://www.neopets.com/prehistoric/omelette.phtml'},
        {'url': '/static/images/grave_digger.png', 'alt': 'Grave Danger', 'link': 'https://www.neopets.com/halloween/gravedanger/'},
        {'url': '/static/images/grumpy_king.png', 'alt': 'Grumpy King', 'link': 'https://www.neopets.com/medieval/grumpyking.phtml'},
        # {'url': '/static/images/', 'alt': '', 'link': ''},        
        # Add more images here...
    ]
    return render_template('gallery.html', images=images)    