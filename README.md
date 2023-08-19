# Criando um Sistema Bancário com Python

Desafio de projeto - 1º Desafio do módulo "Dominando o Python para Ciência de Dados".

Consiste em uma aplicação simples com interação via terminal simulando as operações de `Saque`, `Depósito` e `Extrato` de uma conta bancária.

---

## Requisitos

- Python3

---

## Execução

No terminal execute o arquivo `banking_system.py` através do comando `Python3 banking_system.py`

---

## Regras de negócio

- Depósito
    - Aceita apenas valores maiores que 0 (zero)
    - Todo depósito deve constar na operação de extrato
- Saque
    - Limite de 3 saques
    - O valor máximo por saque é R$ 500.00
    - Não permitir o saque caso não haja saldo suficiente
    - Todo saque deve constar na operação de extrato
- Extrato
    - Deve listar todos os saques e depósitos realizados
    - Deve exibir o saldo atual no final do extrato
    - Se não houver movimentação, deve exibir a mensagem `"Não foram realizadas movimentações"`
    - Todos os valores devem estar no formato R$ xxx.xx

---

## Autor

- [@Rogério Lima](https://github.com/RogerioLima)
