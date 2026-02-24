from database import conectar, criar_tabela

criar_tabela()

def adicionar_funcionario(nome, cargo, salario):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)",
        (nome, cargo, salario)
    )
    conexao.commit()
    conexao.close()

def listar_funcionarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    conexao.close()
    return funcionarios

# Teste
adicionar_funcionario("João", "Analista", 3500)
adicionar_funcionario("Maria", "Gerente", 6000)

for f in listar_funcionarios():
    print(f)