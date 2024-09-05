
# CRUD com Python usando MySQL

Esse CRUD criado em Python em algo bem simples, onde você faz uma pequena interação com apenas uma tabela no MySQL.


## Autores

- [Francisco Gomes](https://www.linkedin.com/in/fgsj-developer/)


## Referência

 - [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
 - [W3schools - MySQL](https://www.w3schools.com/mysql/default.asp)

## Uma breve orientação sobre o fluxo para o desenvolvimento do projeto

A IDE que eu estou utilizando é o PyCharm na versão Community, porém a lógica de construção é a mesma para qualquer IDE
Com a criação do projeto, na imagem abaixo, você deverá clicar com o botão direito sobre o nome do projeto e criar um novo diretório (pasta) com o nome que você quiser
E dentro do diretório, você precisa criar um arquivo Python 

![image](https://github.com/user-attachments/assets/05af58a5-1d65-4eb6-8099-ca31f59e9920)

## Após isso vamos para o código

O início do código 
## Certifique-se que você já tenha instalado o Driver do MySQL (o pip intall mysql-connector-python)
![image](https://github.com/user-attachments/assets/d2447c1e-1686-472a-ba29-5fafb5a8f218)

## Caso haja problema ainda segue no uso do módulo do MySQL
### Verifique se nas configurações do interpretador consta os plugins do MySQL
![image](https://github.com/user-attachments/assets/2b959818-0a9b-48b0-b09d-cbfbbfef4fbb)
![image](https://github.com/user-attachments/assets/52df61bd-4752-40c4-80bf-01697228c78e)

## Nesse código vamos destacar as 4 operações do CRUD
### Nas operações de qualquer atualização no banco de dados sendo o CREATE, UPDATE e DELETE devemos utilizar a operação commit para concretizar a operação realizada, você pode verificar isso na última linha de código em cada operação, também se faz necessário
### Entender um pouco de SQL, visto que na primeira linha de cada comando, é uma instrução SQL, e a cada vez que você executar o código com a operação desejada e o terminal não acusar nenhum erro, pode ir no banco de dados verificar o resultado da operação.

![image](https://github.com/user-attachments/assets/cac23200-7e14-46ff-9e0b-698a70c8a777)



