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
        # {'url': '/static/images/', 'alt': '', 'link': ''},
        # Add more images here...
    ]
    return render_template('gallery.html', images=images)    