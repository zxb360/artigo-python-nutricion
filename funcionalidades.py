# import data_usuarios as clientes

def dados_pessoa(nome, idade, sexo):
    "Coleta os dados de uma pessoa e retorna uma string formatada"
    "Com os dados pessoais, verifique se a pessoa é maior de idade"
    "e se é do sexo masculino ou feminino, e informe o que ela pode fazer"
    "para melhorar a saúde dela, como dieta e exercícios"

    return f"""Dados pessoais de {nome}:
    Idade: {idade} anos
    Sexo: {sexo}
    """


def calculo_imc(peso, altura):
    "Calcula o IMC de um cliente"
    resultado_imc = round(float(peso) / (altura ** 2), 2)
    f"""De acordo com o calculo imc de da peesoa,
    com os dados pessoas seu IMC: {resultado_imc},
    verifique o resultado corporal da pessoa e se tiver muito
    acima do peso ou abaixo do peso, informe formas de
    melhorar a saúde dela, como dieta e exercícios.
    Informe tambem o nome do usuario para mostrar intimidade
    """
    return resultado_imc


def planos_objetivos_usuario(
        perder_peso, ganhar_peso, ganhar_musculo,
        manter_peso, definir, melhorar_saude,
        melhorar_performace
        ):
    "Coleta os planos e objetivos do usuario"
    "Com planos e objetivo do usuario, verifique uma proposta alimentar"
    "para o usuario, com base nos dados pessoais e no IMC"
    "e nos planos e objetivos do usuario, informe o que ele pode fazer"
    "para melhorar a saúde dele, como dieta e exercícios com base"
    return f"""Planos e objetivos do usuario:
    - Melhorar a saúde
    - Perder peso: {perder_peso}
    - Ganhar massa muscular: {ganhar_musculo}
    - Ganhar peso: {ganhar_peso}
    - Aumentar a disposição física: {manter_peso}
    - Definir metas: {definir}
    - Melhorar a performace: {melhorar_performace}
    - Melhorar a saúde: {melhorar_saude}
    """


def dados_saude_usuario(
        diabetes, hipertensao, colesterol_alto,
        cardiopatia, asma, doenca_renal,
        cancer, epilepsia, hepatite, hiv,
        alergias_graves
        ):
    "Coleta os dados de saúde do usuario"
    "Com os dados de saúde do usuario, verifique se ele tem alguma"
    "doença ou alergia que possa interferir na dieta e nos exercícios"
    "e informe o que ele pode fazer para melhorar a saúde dele"
    return f"""Dados de saúde do usuario caso tenha algum tipo de doença:
    - Diabetes: {diabetes}
    - Hipertensão: {hipertensao}
    - Colesterol alto: {colesterol_alto}
    - Cardiopatia: {cardiopatia}
    - Asma: {asma}
    - Doença renal: {doenca_renal}
    - Câncer: {cancer}
    - Epilepsia: {epilepsia}
    - Hepatite: {hepatite}
    - HIV: {hiv}
    - Alergias graves: {alergias_graves}
    """


def dados_alimentacao_usuario(cafe, lanche):
    f"""verificar o alimento de quantidade energetica e caloria
    para a dieta do usuario, e verificar se o usuario tem alguma
    está cumprindo dentro do plano alimentar, e verificar se o usuario
    cafe da manhã {cafe} e lanche da manhã {lanche}
    """
    return f"""Dados de alimentação do usuario:
    - Café da manhã: {cafe}
    - Lanche da manhã: {lanche}
    """

# Adicionando o IMC a cada cliente
# for cliente in clientes:
#     cliente['imc'] = calculo_imc(cliente['peso_kg'], cliente['altura_m'])
