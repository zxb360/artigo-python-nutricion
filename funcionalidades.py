# import data_usuarios as clientes


def calculo_imc(nome, peso, altura):
    "Calcula o IMC de um cliente"
    altura = float(altura)
    return f"""De acordo com o calculo imc {nome}:
    O seu peso é {peso} kg e a sua altura é {altura} m
    seu IMC é de {round(float(peso) / (altura ** 2), 2)}
    verifique o resultado corporal da pessoa e se tiver muito
    acima do peso ou abaixo do peso, informe formas de
    melhorar a saúde dela, como dieta e exercícios.
    Informe tambem o nome do usuario para mostrar intimidade
    """


# Adicionando o IMC a cada cliente
# for cliente in clientes:
#     cliente['imc'] = calculo_imc(cliente['peso_kg'], cliente['altura_m'])
