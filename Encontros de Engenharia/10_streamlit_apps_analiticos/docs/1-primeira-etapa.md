# Streamlit
O Streamlit é um framework Python voltado para a criação rápida de aplicações web interativas, especialmente utilizado em Data Science, Data Analytics e Machine Learning. Seu principal diferencial é permitir que aplicações web sejam construídas apenas com Python, sem a necessidade de conhecimentos prévios em HTML, CSS ou JavaScript.

A filosofia do Streamlit é simples:
👉 o script Python é a aplicação.


## Criando a primeira aplicação

O primeiro passo é criar um arquivo Python, normalmente chamado de main.py. Esse arquivo será o ponto de entrada da aplicação, responsável por definir toda a interface e lógica da app.

Em seguida, importamos a biblioteca Streamlit e utilizamos a função write(), que é uma das funções mais genéricas da ferramenta, responsável por renderizar conteúdos na interface.

```python
import streamlit as st

st.write("Hello World")
```

Para executar a aplicação, utilizamos o comando:
```bash
streamlit run main.py
```
Ao rodar esse comando:
- O Streamlit inicia um servidor web local
- Uma aplicação é disponibilizada via localhost
- Uma aba do navegador padrão é aberta automaticamente (caso isso não aconteça, a URL será exibida no terminal)

Esse modelo segue o padrão de aplicações web cliente-servidor, onde:
- O backend é o próprio script Python
- O frontend é gerado automaticamente pelo Streamlit no navegador

## Modelo reativo e execução do código
Um conceito fundamental do Streamlit é o seu modelo de execução reativo. Mudanças no código e interação do usuário na interface gerada irão se propagar no web browser automaticamente, sem necessidade de reexecução, isso pois o Streamlit reexecuta inteiramente o arquivo python quando algo muda. Todo o arquivo Python é reexecutado do início ao fim.

## A função write()

A função st.write() é extremamente flexível e inteligente. Ela atua como um renderizador genérico, detectando automaticamente o tipo do objeto passado e exibindo-o da forma mais adequada.

Ela suporta, por exemplo, Strings (texto), Números, Booleanos, Listas, Dicionários, Objetos Pandas, Objetos Numpy, Resultados de Expresões Python


Exemplos:
```python
st.write(42)
st.write([1, 2, 3])
st.write({"nome": "Ana", "idade": 30})
```

Essa flexibilidade torna o Streamlit especialmente produtivo para exploração de dados, prototipação e demonstrações interativas.

