# 📢 Sistema de Ouvidoria Universitária

Este é um sistema simples de **ouvidoria universitária**, desenvolvido em Python, com integração a banco de dados MySQL. Ele permite cadastrar, listar, filtrar, pesquisar e excluir manifestações como **reclamações**, **sugestões** e **elogios**.

## 🚀 Funcionalidades

- 📋 Listagem de todas as manifestações
- 🔍 Filtragem por tipo (reclamação, sugestão ou elogio)
- ➕ Cadastro de novas manifestações
- 📊 Exibição da quantidade total de manifestações
- 🧭 Pesquisa de manifestação por código
- ❌ Exclusão de manifestação pelo código

## 🛠️ Tecnologias utilizadas

- Python 3
- MySQL
- Biblioteca personalizada de acesso ao banco (`operacoesbd.py`)

## 📂 Estrutura do Projeto

## 🗃️ Banco de Dados

Certifique-se de ter um banco MySQL com a seguinte base e tabela:

### Banco: `ouvidoriabd`

### Tabela: `comentarios`
```sql
CREATE TABLE comentarios (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    descricao TEXT NOT NULL,
    autor VARCHAR(100),
    ouvidor VARCHAR(100),
    tipo VARCHAR(50)
);


