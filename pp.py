from flask import Flask, render_template, request, redirect, url_for, flash
from mysql import connector

app = Flask(__name__)
app.secret_key = 'chave_secreta'

# Simulação de dados para exemplo
resgates = []
tratamentos = []
campanhas = []
estoque = []
animais_adotados = []  # Lista para armazenar os animais adotados

@app.route("/")
def home():
    return render_template("index.html", resgates=resgates, tratamentos=tratamentos, campanhas=campanhas, estoque=estoque, animais_adotados=animais_adotados)

@app.route("/cadastro", methods=["POST"])
def cadastro():
    cliente = request.form.get("cliente")
    cpf = request.form.get("cpf")
    rua = request.form.get("rua")
    bairro = request.form.get("bairro")
    cidade = request.form.get("cidade")
    uf = request.form.get("uf")
    contato = request.form.get("contato")

    dados = (cliente, cpf, rua, bairro, cidade, uf, contato)

    connect = connector.connect(
        host="localhost",
        database="ong",
        user="root",
        password="Myxboxone1."
    )

    cursor = connect.cursor()

    query = """
        INSERT INTO cadastro (cliente, cpf, rua, bairro, cidade, uf, telefone)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, dados)

    connect.commit()

    cursor.close()
    connect.close()

    flash("Usuário cadastrado com sucesso!")
    return redirect(url_for("home") + "#resgates")

@app.route("/cadastro_animal", methods=["POST"])
def cadastro_animal():
    especie = request.form.get("especie")
    raca = request.form.get("raca")
    porte = request.form.get("porte")
    sexo = request.form.get("sexo")  # Pode ser 'M' ou 'F'
    idade_aproximada = request.form.get("idade_aproximada")
    estado_saude = request.form.get("estado_saude")
    local_resgate = request.form.get("local_resgate")
    data_resgate = request.form.get("data_resgate")  # No formato 'YYYY-MM-DD'

    # Dados a serem inseridos na tabela
    dados = (especie, raca, porte, sexo, idade_aproximada, estado_saude, local_resgate, data_resgate)

    # Conexão com o banco de dados
    connect = connector.connect(
        host="localhost",
        database="ong",
        user="root",
        password="Myxboxone1."
    )

    cursor = connect.cursor()

    query = """
        INSERT INTO Animal (especie, raca, porte, sexo, idade_aproximada, estado_saude, local_resgate, data_resgate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, dados)

    connect.commit()

    cursor.close()
    connect.close()

    flash("Animal cadastrado com sucesso!")
    return redirect(url_for("home") + "#resgates")

@app.route("/cadastro_adotante", methods=["POST"])
def cadastro_adotante():
    nome = request.form.get("nome")
    endereco = request.form.get("endereco")
    id_cliente = request.form.get("id_cliente")  # Esse será o ID do cliente relacionado

    dados_adotante = (nome, endereco, id_cliente)

    connect = connector.connect(
        host="localhost",
        database="ong",
        user="root",
        password="Myxboxone1."
    )

    cursor = connect.cursor()

    query = """
        INSERT INTO Adotante (nome, endereco, id_cliente)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, dados_adotante)

    connect.commit()

    cursor.close()
    connect.close()

    flash("Adotante cadastrado com sucesso!")
    return redirect(url_for("home") + "#adocao")  # Redireciona para a seção de adoção

@app.route("/cadastro_adocao", methods=["POST"])
def cadastro_adocao():
    id_animal = request.form.get("id_animal")
    id_adotante = request.form.get("id_adotante")
    data_adocao = request.form.get("data_adocao")
    termo_assinado = request.form.get("termo_assinado")

    dados_adocao = (id_animal, id_adotante, data_adocao, termo_assinado)

    # Conectar ao banco de dados
    connect = connector.connect(
        host="localhost",
        database="ong",
        user="root",
        password="Myxboxone1."
    )

    cursor = connect.cursor()

    # Inserir a adoção na tabela Adocao
    query = """
        INSERT INTO Adocao (id_animal, id, data_adocao, termo_assinado)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, dados_adocao)

    # Commit para salvar no banco
    connect.commit()

    cursor.close()
    connect.close()

    flash("Adoção registrada com sucesso!")
    return redirect(url_for("home") + "#adocao")  # Redireciona para a seção de adoção

@app.route("/cadastro_veterinario", methods=["POST"])
def cadastro_veterinario():
    crmv = request.form.get("crmv")
    nome_veterinario = request.form.get("nome_veterinario")

    dados = (crmv, nome_veterinario)

    connect = connector.connect(
        host="localhost",
        database="ong",
        user="root",
        password="Myxboxone1."
    )

    cursor = connect.cursor()

    query = """
        INSERT INTO Veterinario (crmv, nome_veterinario)
        VALUES (%s, %s)
    """
    cursor.execute(query, dados)

    connect.commit()

    cursor.close()
    connect.close()

    flash("Veterinário cadastrado com sucesso!")
    return redirect(url_for("home") + "#veterinarios")


@app.route("/cadastro_tratamento", methods=["POST"])
def cadastro_tratamento():
    id_animal = request.form.get("id_animal")
    data_tratamento = request.form.get("data_tratamento")
    tipo_procedimento = request.form.get("tipo_procedimento")
    crmv = request.form.get("crmv")  # Novo campo para armazenar o CRMV do veterinário responsável

    dados_tratamento = (id_animal, data_tratamento, tipo_procedimento, crmv)

    # Conectar ao banco de dados
    connect = connector.connect(
        host="localhost",
        database="ong",
        user="root",
        password="Myxboxone1."
    )

    cursor = connect.cursor()

    # Inserir o tratamento na tabela Tratamento
    query = """
        INSERT INTO Tratamento (id_animal, data_tratamento, tipo_procedimento, crmv)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, dados_tratamento)

    # Commit para salvar no banco
    connect.commit()

    cursor.close()
    connect.close()

    flash("Tratamento registrado com sucesso!")
    return redirect(url_for("home") + "#tratamento")


@app.route("/cadastro_campanha", methods=["POST"])
def cadastro_campanha():
    tipo_campanha = request.form.get("tipo_campanha")
    data_campanha = request.form.get("data_campanha")
    local_campanha = request.form.get("local_campanha")
    id_animal = request.form.get("id_animal")
    
    dados_campanha = (tipo_campanha, data_campanha, local_campanha, id_animal)
    
    # Conectar ao banco de dados
    connect = connector.connect(
        host="localhost",
        database="ong",
        user="root",
        password="Myxboxone1."
    )
    
    cursor = connect.cursor()
    
    # Inserir a campanha na tabela Campanha
    query = """
        INSERT INTO Campanha (tipo_campanha, data_campanha, local_campanha, id_animal)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, dados_campanha)
    
    # Commit para salvar no banco
    connect.commit()
    
    cursor.close()
    connect.close()
    
    flash("Campanha registrada com sucesso!")
    return redirect(url_for("home") + "#campanha")  # Redireciona para a seção de campanhas

@app.route("/cadastro_estoque", methods=["POST"])
def cadastro_estoque():
    nome_item = request.form.get("nome_item")
    quantidade_item = request.form.get("quantidade_item")
    id_tratamento = request.form.get("id_tratamento")

    dados_estoque = (nome_item, quantidade_item, id_tratamento)

    connect = connector.connect(
        host="localhost",
        database="ong",
        user="root",
        password="Myxboxone1."
    )

    cursor = connect.cursor()

    query = """
        INSERT INTO Estoque (nome_item, quantidade_item, id_tratamento)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, dados_estoque)

    connect.commit()

    cursor.close()
    connect.close()

    flash("Item de estoque cadastrado com sucesso!")
    return redirect(url_for("home") + "#estoque")  # Redireciona para a seção de estoque


if __name__ == "__main__":
    app.run(debug=True)