from flask import Flask, render_template, request
from utils.aztro_api import get_astrology_data
from utils.llm_interpreter import interpret_with_gemini

app = Flask(__name__)
app.secret_key = "AIzaSyB9G5PKJdlJc4Y8ILLjvKCb3297Jak9oN0sp"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        dob = request.form['dob']
        tob = request.form['tob']
        place = request.form['place']
        query = request.form['query']

        try:
            astro_data = get_astrology_data(dob, tob, place)
            result = interpret_with_gemini(astro_data, query)
        except Exception:
            fallback_input = f"My birth date is {dob}, time {tob}, place {place}. {query}"
            result = interpret_with_gemini({}, fallback_input)

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
