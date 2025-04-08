import google.generativeai as genai
import os
from funcionalidades import calculo_imc
from flask import Flask, render_template, request

model = genai.GenerativeModel('gemini-1.5-flash',
                              generation_config={"temperature": 0.2}
                              )

app = Flask(__name__)
GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


@app.route('/', methods=['GET', 'POST'])
def home():
    response = None
    if request.method == "POST":
        user = calculo_imc(request.form.get('nome'),
                           request.form.get('peso'),
                           request.form.get('altura'))
        # request.form.get('input')
        if user:
            response = generative_response(user)
    return render_template('index.html', response=response)


def generative_response(i):
    response = model.generate_content(i)
    return response.text


if __name__ == "__main__":
    app.run(port=8000, debug=True)
