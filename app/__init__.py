from flask import Flask, render_template, current_app, request, redirect
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__)
Bootstrap(app)

booze_dict = {
	'a': ["Absintti", "Aplari", "Akvavit" ],
	'b': ["Bourbon", "Brandy", "Bailey's", "Bols" ],
	'c': ["Charteaux", "Coca-Cola", "Campari", "Calvados", "Cointreau"],
	'd': ["Doris", "Dooley's", "Drambuje"],
	'e': ["ES"],
	'f': ["Ferra", "Fisu", "Fireball"],
	'g': ["Grappa", "Gin", "Gambina", "Glögi"],
	'h': ["Huttunen", "Hendrick's", "Hennessey"],
	'i': ["Inkivääriolut", "IPA"],
	'j': ["Jallu", "Jekku", "Jack Daniels"],
	'k': ["Kahlua", "Konjakki", "Kerma"],
	'l': ["Likööri", "Lonkero", "Lager"],
	'm': ["Munaviina", "Maito", "Malibu", "Metaxa", "Minttu", "Mehu"],
	'n': ["Naga Shot", "Navy Jerry"],
	'o': ["Olut", "Ouzo", "Omenamehu"],
	'p': ["Punkku", "Punssi", "Pastis", "Piimä", "Portviini"],
	'q': ["Quark"],
	'r': ["Rommi", "Red Bull", "Rose"],
	's': ["Sake", "Siideri", "Sherry", "Salmari", "Sambuca"],
	't': ["Tequila", "Terva"],
	'u': ["Unicum", "UFO"],
	'v': ["Viski", "Vodka", "Valkkari", "Vissy", "Vaniljakossu", "Vermutti", "Vana Tallinn"],
	'w': ["Waldemar"],
	'x': ["XO", "Xanté"],
	'y': ["Yrttisnapsi"],
	'z': ["Zubrowka"]
}

@app.route('/', methods=['GET'])
def index():
	if 'name' in request.args:
		name = request.args.get('name')
		boozes = ""
		for letter in name.lower():
			boozes = boozes + random.choice(booze_dict[letter]) + ","
		return boozes
	return "Name parameter missing!"