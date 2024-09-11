
import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('adote_animais.db')
cursor = conn.cursor()

# Criação da tabela de Animais
cursor.execute('''
CREATE TABLE IF NOT EXISTS Animais (
    id_animal INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    especie TEXT NOT NULL,
    raca TEXT,
    idade INTEGER,
    data_resgate DATE NOT NULL,
    status TEXT DEFAULT 'Em Tratamento'
)
''')

# Criação da tabela de Adoções
cursor.execute('''
CREATE TABLE IF NOT EXISTS Adocoes (
    id_adocao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_animal INTEGER,
    nome_adotante TEXT NOT NULL,
    data_adocao DATE NOT NULL,
    FOREIGN KEY(id_animal) REFERENCES Animais(id_animal)
)
''')

# Função para cadastrar animal
def cadastrar_animal(nome, especie, raca, idade, data_resgate):
    cursor.execute('''INSERT INTO Animais (nome, especie, raca, idade, data_resgate)
                      VALUES (?, ?, ?, ?, ?)''', (nome, especie, raca, idade, data_resgate))
    conn.commit()
    print("Animal cadastrado com sucesso!")

# Função para registrar adoção
def registrar_adocao(id_animal, nome_adotante, data_adocao):
    cursor.execute('''INSERT INTO Adocoes (id_animal, nome_adotante, data_adocao)
                      VALUES (?, ?, ?)''', (id_animal, nome_adotante, data_adocao))
    conn.commit()
    print("Adoção registrada com sucesso!")

# Função para listar animais
def listar_animais():
    cursor.execute("SELECT * FROM Animais")
    animais = cursor.fetchall()
    for animal in animais:
        print(animal)

# Fechando a conexão com o banco de dados
conn.close()
