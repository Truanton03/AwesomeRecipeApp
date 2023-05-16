# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from recipes import recipes

app = Flask(__name__)
CORS(app)

# Get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipes)

# Get a specific recipe by ID
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = [recipe for recipe in recipes if recipe['id'] == recipe_id]
    if len(recipe) == 0:
        return jsonify({'error': 'Recipe not found'})
    return jsonify(recipe[0])

# Add a new recipe
@app.route('/recipes', methods=['POST'])
def add_recipe():
    new_recipe = {
        'id': recipes[-1]['id'] + 1,
        'name': request.json['name'],
        'ingredients': request.json['ingredients'],
        'instructions': request.json['instructions'],
        'cuisine': request.json['cuisine']
    }
    recipes.append(new_recipe)
    return jsonify({'message': 'Recipe added successfully'})

# Update an existing recipe
@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = [recipe for recipe in recipes if recipe['id'] == recipe_id]
    if len(recipe) == 0:
        return jsonify({'error': 'Recipe not found'})
    recipe[0]['name'] = request.json['name']
    recipe[0]['ingredients'] = request.json['ingredients']
    recipe[0]['instructions'] = request.json['instructions']
    recipe[0]['cuisine'] = request.json['cuisine']
    return jsonify({'message': 'Recipe updated successfully'})

# Delete a recipe
@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = [recipe for recipe in recipes if recipe['id'] == recipe_id]
    if len(recipe) == 0:
        return jsonify({'error': 'Recipe not found'})
    recipes.remove(recipe[0])
    return jsonify({'message': 'Recipe deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

# recipes.py (Data for testing)
recipes = [
    {
        'id': 1,
        'name': 'Spaghetti Bolognese',
        'ingredients': ['spaghetti', 'ground beef', 'tomato sauce', 'onion', 'garlic'],
        'instructions': 'Cook spaghetti. Brown ground beef with onion and garlic. Add tomato sauce. Serve over cooked spaghetti.',
        'cuisine': 'Italian'
    },
    {
        'id': 2,
        'name': 'Chicken Tikka Masala',
        'ingredients': ['chicken', 'yogurt', 'tomato sauce', 'onion', 'garam masala'],
        'instructions': 'Marinate chicken in yogurt and spices. Grill chicken. Simmer tomato sauce with onions and spices. Add grilled chicken. Serve with rice.',
        'cuisine': 'Indian'
    }
]
