import google.generativeai as genai
import os
from flask import Flask, render_template, request

model = genai.GenerativeModel('gemini-pro',
                              generation_config={"temperature": 0.5}
                              )

app = Flask(__name__)
GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


@app.route('/', methods=['GET', 'POST'])
def home():
    response = None
    if request.method == "POST":
        input = request.form['input']  # request.form.get('input')
        if input:
            response = generative_response(input)
    return render_template('index.html', response=response)


def generative_response(i):
    response = model.generate_content(i)
    return response.text


if __name__ == "__main__":
    app.run(debug=True)
