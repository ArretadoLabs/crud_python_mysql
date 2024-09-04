import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='IEtaps10!@#',
    database='bdcrud',
)

cursor = connection.cursor()

#---------------------------------- final do código
cursor.close()
connection.close()


#CREATE
#nome_produto = "chocolate"
#valor = 5
#command = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(command)
#connection.commit()


#READ
#command = f'SELECT * FROM vendas'
#cursor.execute(command)
#resultado = cursor.fetchall() #O comando Fetchall é para operações de leitura
#print(resultado)

#UPDATE
#command = f'UPDATE vendas SET valor = 10 WHERE idVendas = 1 '
#cursor.execute(command)
#connection.commit()

#DELETE
#command = f'DELETE FROM vendas WHERE idVendas = 1'
#cursor.execute(command)
#connection.commit()


