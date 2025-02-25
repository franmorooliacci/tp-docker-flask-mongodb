from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient(host='mongo', port=27017, username='user',
                     password='password', authSource='admin')
db = client.gamesdb
games_collection = db.games


@app.route('/')
def index():
    games = list(games_collection.find())
    return render_template('index.html', games=games)


@app.route('/add', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        game = {
            "nombre": request.form['nombre'],
            "min_jugadores": int(request.form['min_jugadores']),
            "max_jugadores": int(request.form['max_jugadores']),
            "edad_min": int(request.form['edad_min']),
            "pais": request.form['pais'],
            "costo": float(request.form['costo'])
        }
        games_collection.insert_one(game)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/game/<game_id>')
def game_detail(game_id):
    game = games_collection.find_one({"_id": ObjectId(game_id)})
    if not game:
        return "Juego no encontrado", 404
    return render_template('details.html', game=game)


@app.route('/delete/<game_id>', methods=['POST'])
def delete_game(game_id):
    games_collection.delete_one({"_id": ObjectId(game_id)})
    return redirect(url_for('index'))


@app.route('/edit/<game_id>', methods=['GET', 'POST'])
def edit_game(game_id):
    game = games_collection.find_one({"_id": ObjectId(game_id)})
    if request.method == 'POST':
        update = {
            "nombre": request.form['nombre'],
            "min_jugadores": int(request.form['min_jugadores']),
            "max_jugadores": int(request.form['max_jugadores']),
            "edad_min": int(request.form['edad_min']),
            "pais": request.form['pais'],
            "costo": float(request.form['costo'])
        }
        games_collection.update_one(
            {"_id": ObjectId(game_id)}, {"$set": update})
        return redirect(url_for('index'))
    return render_template('edit.html', game=game)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
