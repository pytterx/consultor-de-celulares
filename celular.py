import sqlite3

# Conectar-se ao banco de dados local
conn = sqlite3.connect('celulares.db')
cursor = conn.cursor()


# Criar a tabela de celulares, caso ainda não exista
cursor.execute('''
    CREATE TABLE IF NOT EXISTS celulares (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        marca TEXT NOT NULL,
        giga TEXT NOT NULL,
        processador TEXT NOT NULL,   
        memoria_ram TEXT NOT NULL,
        preco REAL NOT NULL
    )
''')

# Inserir dados na tabela
cursor.execute('''
    INSERT OR IGNORE INTO celulares(nome, marca, giga, processador, memoria_ram, preco)
    VALUES("Iphone 13", "Apple", "128G,256G,512,1TB", "Chip A15 Bionic", "6G", 7000),
            ("Samsung Galaxy S21 Ultra", "Samsung", "128G,256G,512G", "Exynos 2100/Snapdragon 888", "12G ou 16G", 2000), 
            ("Google Pixel 6 Pro", "Google", "128G", "Google Tensor", "12G", 2000),
            ("OnePlus 9 Pro", "OnePlus", "128G", "Qualcomm Snapdragon 888", "8G ou 12G", 1000),
            ("Xiaomi Mi 11 Ultra", "Xiaomi", "128G", "Qualcomm Snapdragon 888", "8G ou 12G",2000),
            ("Sony Xperia 1 III", "Sony", "128G", "Qualcomm Snapdragon 888", "12G", 3500),
            ("Huawei P50 Pro", "Huawei", "128G", "Qualcomm Snapdragon 888 (Versão 4G) / Kirin 9000 (Versão 5G)", "8G ou 12G", 3000),
            ("Samsung Galaxy Z Fold 3", "Samsung", "128G", "Qualcomm Snapdragon 888", "12G", 2500),
            ("iPhone 13 Mini", "Apple", "128G", "Chip A15 Bionic", "4G", 2000),
            ("Xiaomi Redmi Note 11 Pro", "Xiaomi", "128G", "Qualcomm Snapdragon 695", "6G ou 8G", 2000)
''')

# Fechar comunicação com o db
conn.commit()
conn.close()

# Pedir ao usuário para inserir um nome
nome = input("Qual é o nome do celular? ")

# Consultar o db 
conn = sqlite3.connect('celulares.db')
cursor = conn.cursor()
cursor.execute('''
    SELECT nome, marca, giga, processador, memoria_ram, preco
    FROM celulares
    WHERE nome = ? 
''', (nome,))
resultado = cursor.fetchone()
conn.close()

# Verificar se foi encontrado
if resultado is None:
    print('Celular não encontrado')
    exit()

# Exibir informações
nome, marca, giga, processador, memoria_ram, preco = resultado
print(f'Nome: {nome}')
print(f'Marca: {marca}')
print(f'Giga: {giga}')
print(f'Processador: {processador}')
print(f'Memória RAM: {memoria_ram}')
print(f'Preço: {preco}')
