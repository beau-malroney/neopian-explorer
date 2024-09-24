import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

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
        {'url': '/static/images/daily_interest.png', 'alt': 'Daily Interest', 'link': 'https://www.neopets.com/bank.phtml'},
        {'url': '/static/images/coltzans_shrine.png', 'alt': "Coltzan's Shrine", 'link': 'https://www.neopets.com/desert/shrine.phtml'},
        {'url': '/static/images/deserted_tomb.png', 'alt': 'Deserted Tomb', 'link': 'https://www.neopets.com/worlds/geraptiku/tomb.phtml'},
        {'url': '/static/images/forgotten_shore.png', 'alt': 'Forgotten Shore', 'link': 'https://www.neopets.com/pirates/forgottenshore.phtml'},
        {'url': '/static/images/fruit_machine.png', 'alt': 'Fruit Machine', 'link': 'https://www.neopets.com/desert/fruit/index.phtml'},
        {'url': '/static/images/giant_omelette.png', 'alt': 'Giant Omelette', 'link': 'https://www.neopets.com/prehistoric/omelette.phtml'},
        {'url': '/static/images/grave_digger.png', 'alt': 'Grave Danger', 'link': 'https://www.neopets.com/halloween/gravedanger/'},
        {'url': '/static/images/grumpy_king.png', 'alt': 'Grumpy King', 'link': 'https://www.neopets.com/medieval/grumpyking.phtml'},
        {'url': '/static/images/jelly.png', 'alt': 'Giant fn Jelly', 'link': 'https://www.neopets.com/jelly/jelly.phtml'},
        {'url': '/static/images/void_within.png', 'alt': 'Void Within', 'link': 'https://www.jellyneo.net/?go=the_void_within&id=essence_collection'},
        {'url': '/static/images/marrow.png', 'alt': 'Guess the weight of the Marrow', 'link': 'https://www.neopets.com/medieval/guessmarrow.phtml'},
        {'url': '/static/images/healing_springs.png', 'alt': 'Healing Springs', 'link': 'https://www.neopets.com/faerieland/springs.phtml'},
        {'url': '/static/images/meteor.png', 'alt': 'Meteor', 'link': 'https://www.neopets.com/moon/meteor.phtml'},
        {'url': '/static/images/money_tree.png', 'alt': 'Money Tree', 'link': 'https://www.neopets.com/donations.phtml'},
        {'url': '/static/images/mysterious_negg_cave.png', 'alt': 'Mysterious Negg Cave', 'link': 'https://www.neopets.com/shenkuu/neggcave/'},
        {'url': '/static/images/slorg.png', 'alt': 'Rich Slorg', 'link': 'https://www.neopets.com/shop_of_offers.phtml?slorg_payout=yes'},
        {'url': '/static/images/', 'alt': 'Monthly Freebies', 'link': 'https://www.neopets.com/freebies/'},
        {'url': '/static/images/discarded_plush.png', 'alt': 'Discarded Plushie', 'link': 'https://www.neopets.com/faerieland/tdmbgpop.phtml'},
        {'url': '/static/images/tombola.png', 'alt': 'Tombola', 'link': 'https://www.neopets.com/island/tombola.phtml'},
        {'url': '/static/images/trudys_surprise.png', 'alt': "Trudy's Surprise", 'link': 'https://www.neopets.com/trudys_surprise.phtml'},
        {'url': '/static/images/tarlas_treasures.png', 'alt': "Tarla's Treasures", 'link': 'https://www.neopets.com/freebies/tarlastoolbar.phtml'},
        {'url': '/static/images/wise_king.png', 'alt': 'Wise Old King', 'link': 'https://www.neopets.com/medieval/wiseking.phtml'},
        {'url': '/static/images/vortex.png', 'alt': 'Fishing Vortex', 'link': 'https://www.neopets.com/water/fishing.phtml'},        
        {'url': '/static/images/fashion.png', 'alt': 'Fashion Fever', 'link': 'https://www.neopets.com/games/game.phtml?game_id=805'},
        {'url': '/static/images/buried_treasure.png', 'alt': 'Buried Treasure', 'link': 'https://www.neopets.com/pirates/buriedtreasure/index.phtml'},
        {'url': '/static/images/employment.png', 'alt': 'Employment Agency', 'link': 'https://www.neopets.com/faerieland/employ/employment.phtml'},
        {'url': '/static/images/fairie_caverns.png', 'alt': 'Faerie Cavern', 'link': 'https://www.neopets.com/faerieland/caverns/index.phtml'},
        {'url': '/static/images/stocks.png', 'alt': 'Stock Market - Bargain', 'link': 'https://www.neopets.com/stockmarket.phtml?type=list&search=%&bargain=true'},
        {'url': '/static/images/test_your_strength.png', 'alt': 'Test Your Strength', 'link': 'https://www.neopets.com/halloween/strtest/index.phtml'},
        {'url': '/static/images/', 'alt': 'Battledome', 'link': 'https://www.neopets.com/dome/'},
        {'url': '/static/images/snowager.png', 'alt': 'Snowager', 'link': 'https://www.neopets.com/winter/snowager.phtml'},
        {'url': '/static/images/mystery_island_training.png', 'alt': 'Mystery Island Training School', 'link': 'https://www.neopets.com/island/training.phtml'},
        {'url': '/static/images/swashbuckling_school.png', 'alt': 'Swashbuckling Academy', 'link': 'https://www.neopets.com/pirates/academy.phtml'},
        # {'url': '/static/images/', 'alt': '', 'link': ''},
        # Add more images here...
    ]
    return render_template('gallery.html', images=images)

# Main Function, Runs at http://0.0.0.0:8000
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)    