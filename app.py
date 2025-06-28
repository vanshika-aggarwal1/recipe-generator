from boltiotai import openai
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

def generateRecipe(ingredients) :
    try:
        response = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": "You are a helpful cooking assistant"
            }, {
                "role":
                "user",
                "content":
                f"Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Share the recipe in a step-by-step manner. Here are the items available: {ingredients}, Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil"
            }])
        return response['choices'][0]['message']['content']
    except Exception as e:
        return "Error Generated"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods = ['POST'])
def generate():
    data = request.get_json()
    ingredients = data.get('ingredients', '')
    recipe = generateRecipe(ingredients)
    return jsonify({'recipe': recipe})

if __name__ == '__main__':
    app.run(debug = True)

