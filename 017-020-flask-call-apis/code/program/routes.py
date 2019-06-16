from program import app
from flask import render_template, request, jsonify
from datetime import datetime
import requests
import json



@app.route('/')
@app.route('/index')

def index():
    timenow = str(datetime.today())
    return render_template('index.html', time=timenow)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/chuck')
def chuck():
    joke = get_chuck_joke()
    return render_template('chuck.html', joke=joke)

def get_chuck_joke():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    data = r.json()
    return data['value']

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    pokemon = []
    #poke_ability = []
    if request.method == 'POST' and 'pokecolour' in request.form:
        colour = request.form.get('pokecolour')
        pokemon = get_poke_colours(colour)
        #poke_ability = get_poke_abilities(pokemon)
    
    
    return render_template('pokemon.html', pokemon=pokemon)
    

def get_poke_colours(colour):
    r = requests.get('https://pokeapi.co/api/v2/pokemon-color/' + colour.lower())
    pokedata = r.json()
    pokemon = []

    for i in pokedata['pokemon_species']:
        pokemon.append(i['name'])
    
    return pokemon

'''def get_poke_abilities(pokemon):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon())
    pokedata = r.json()
    poke_ability = []

    for i in pokedata['abilities']:
        poke_ability.append(i['ability']['name'])

  return poke_ability
'''  
# Error Handling for invalid color
@app.errorhandler(500)
def internal_error(error):
    return render_template('perror.html')