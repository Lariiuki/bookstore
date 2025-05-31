# bookstore
Aula Eback - backend developer

Projeto desenvolvido durante o curso de backend, com o objetivo de praticar e aplicar conceitos fundamentais do desenvolvimento backend utilizando Django e Django REST Framework.

## Funcionalidades

- Cadastro e gerenciamento de produtos (livros)
- Organização dos produtos em categorias
- Registro de pedidos de compra
- Testes automatizados para garantir a qualidade do código

## Tecnologias utilizadas

- Python
- Django 5.2
- Django REST Framework
- SQLite (banco de dados padrão para desenvolvimento)
- Pytest e Django TestCase para testes

## Estrutura

O projeto está organizado em apps Django, com modelos, serializers e testes para cada funcionalidade principal (produtos, categorias e pedidos).# bookstore
Aula Eback - backend developer

Projeto desenvolvido durante o curso de backend, com o objetivo de praticar e aplicar conceitos fundamentais do desenvolvimento backend utilizando Django e Django REST Framework.

## Funcionalidades

- **Cadastro e gerenciamento de produtos (livros):**  
  Permite criar, listar, atualizar e remover livros do catálogo. Cada produto possui atributos como título, preço, descrição e categoria.

- **Organização dos produtos em categorias:**  
  Os livros podem ser agrupados em categorias, facilitando a navegação e filtragem. Cada categoria possui título, slug, descrição e status de ativo.

- **Registro de pedidos de compra:**  
  Implementação de pedidos, permitindo que usuários registrem compras de um ou mais produtos, armazenando informações relevantes do pedido.

- **Testes automatizados:**  
  O projeto inclui testes unitários para garantir o correto funcionamento dos modelos e serializers, aumentando a confiabilidade do sistema.

## Tecnologias utilizadas

- **Python:** Linguagem principal do projeto.
- **Django 5.2:** Framework web utilizado para estruturação do backend.
- **Django REST Framework:** Ferramenta para criação de APIs RESTful.
- **SQLite:** Banco de dados padrão para ambiente de desenvolvimento.
- **Pytest e Django TestCase:** Ferramentas para criação e execução de testes automatizados.

## Estrutura do Projeto

- **product/models.py:**  
  Contém os modelos principais do sistema, como `Product` (livro) e `Category` (categoria).

- **product/serializers/**  
  Inclui serializers para conversão dos modelos em formatos adequados para APIs (JSON), como `ProductSerializer` e `CategorySerializer`.

- **tests/**  
  Diretório com testes automatizados para validar regras de negócio, serialização e funcionamento dos endpoints.

- **product/views.py:**  
  Implementa as views responsáveis pelo tratamento das requisições HTTP relacionadas aos produtos e categorias.

- **product/urls.py:**  
  Define as rotas/endpoints da API para acesso aos recursos do sistema.

## Como executar

1. Clone o repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Execute as migrações com `python manage.py migrate`.
4. Inicie o servidor com `python manage.py runserver`.
5. Execute os testes com `python manage.py test`.

---
Projeto em desenvolvimento para fins educacionais.