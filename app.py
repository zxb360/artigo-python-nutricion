import google.generativeai as genai
import os
# from funcionalidades import calculo_imc  # mas erro
from flask import Flask, render_template, request

model = genai.GenerativeModel('gemini-1.5-flash',
                              generation_config={"temperature": 0.2}
                              )

app = Flask(__name__)
GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


# Está é estrutura incial do projeto, uma função para decisão
def decision_ai(user):
    regras_negocio = """
Você é um assistente de nutrição, que tem como objetivo ajudar os usuários a
 melhorar sua saúde.
Você deve responder apenas perguntas relacionadas a saúde, alimentação e
 exercícios.
"""
    decision_user = model.start_chat(enable_automatic_function_calling=True)
    response = decision_user.send_message(
        f"""Dados do usuario {regras_negocio}, {user}, eu dividir em
        seções para facilitar o entendimento, exemplo ajudaria muito se fosse:
        Nome: {user[0]["dado_pessoal"]["nome"]}
        Peso: {user[0]["imc"]["peso"]},
        Altura: {user[0]["imc"]["altura"]},
        Percebi na resposta que a sempre " ** " é o separador,
        poderia separar sempre que puder em tópicos organizacional para pular
        linha e facilitar o entendimento.""")

    # user.send_message("Reflita e informe caso não haja interação")
    return response.text


@app.route('/', methods=['GET', 'POST'])
def home():
    response = None
    user = [{
        "dado_pessoal": {
            "nome": request.form.get("nome"),
            "idade": request.form.get("idade"),
            "sexo": request.form.get("sexo"),
        },
        "objetivos": {
            "objetivo": request.form.get("objetivo"),
        },
        "imc": {
            "peso": request.form.get("peso"),
            "altura": request.form.get("altura"),
        },
        "saude": {
           "saude_geral": request.form.get("condicoes_medicas"),
        },
        "preferencias": {
            "pref_alimentares": request.form.get("preferencia_alimentar"),
        },
        "atividade_fisicas": {
            "atividade": request.form.get("atividade_fisica"),
        },
        "refeicoes": {
            "cafe_da_manha": request.form.get("cafe"),
            "lanche_manha": request.form.get("lanche_manha"),
        }
    }]

    if request.method == "POST":
        response = decision_ai(user)

    return render_template('index.html', response=response)


# def generative_response(i):
#     response = model.generate_content(i)
#     return response.text


if __name__ == "__main__":
    app.run(port=8000, debug=True)
