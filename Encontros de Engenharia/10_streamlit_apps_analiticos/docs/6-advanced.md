# Boas Práticas no Streamlit: Keys e Cache

Nesta seção, abordamos duas práticas fundamentais para aplicações Streamlit mais estáveis, performáticas e previsíveis:

- Uso de **keys** para identificação de componentes
- Uso de **cache** para otimizar execução e gerenciamento de recursos

---

## Uso de Keys em Componentes

No Streamlit, **cada widget precisa de um identificador único** dentro da aplicação.  
Quando esse identificador não é explícito, o Streamlit tenta inferir automaticamente, o que pode gerar conflitos em aplicações maiores.

### Exemplo sem key explícita

```python
st.button("OK")
st.button("OK")
```

Esse código gera erro, pois o Streamlit não consegue diferenciar dois widgets iguais.

Boa prática: usar `key`

```python
st.button("OK")
st.button("OK", key="btn2")
```

Por que usar keys?

- Evita conflitos entre widgets iguais
- Permite controle explícito do estado do componente
- Facilita manutenção e refatoração
- É essencial em:
  - Loops
  - Componentes dinâmicos
  - Aplicações multipágina
  - Uso avançado de `session_state`

> **Sempre use `key` quando houver qualquer chance de duplicação de widgets.**

---

## Cache de Dados (`st.cache_data`)

O `st.cache_data` é utilizado para **cachear resultados de funções puras**, ou seja:
- Funções que retornam dados
- Sem efeitos colaterais
- Que podem ser recalculadas quando necessário

```python
import time
import streamlit as st

@st.cache_data(ttl=60)
def fetch_data():
    time.sleep(3)
    return {"data": "This is cached data!"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)
```

O que está acontecendo?
- A primeira execução demora 3 segundos
- O resultado é armazenado em cache
- Durante 60 segundos (`ttl=60`):
  - A função não é reexecutada
  - O valor armazenado é reutilizado

Quando usar `cache_data`?
- Consultas em banco de dados
- Chamadas de API
- Processamentos pesados
- Leitura de arquivos imutáveis

---

## Cache de Recursos (`st.cache_resource`)

O `st.cache_resource` é usado para **objetos persistentes e não serializáveis**, como:
- Conexões com banco
- Clientes de API
- Modelos de Machine Learning
- Arquivos abertos

Esses recursos **devem ser reutilizados**, não recalculados.

**Exemplo com Manipulação de Arquivo**

```python
file_path = "text.txt"

@st.cache_resource
def get_file_handler():
    file = open(file_path, "a+")
    return file

file_handler = get_file_handler()
```

Nesse caso:
- O arquivo é aberto apenas uma vez por sessão
- O mesmo handler é reutilizado nas reexecuções


```python
if st.button("Write to File"):
    file_handler.write("Nova linha\n")
    file_handler.flush()
```

- `flush()` garante que o conteúdo seja persistido imediatamente
- O botão dispara apenas a ação, sem recriar o recurso

```python
if st.button("Read File"):
    file_handler.seek(0)
    content = file_handler.read()
    st.text(content)
```

- `seek(0)` move o cursor para o início do arquivo
- Permite leitura completa do conteúdo

```python
st.button("Close File", on_click=file_handler.close)
```

- Uso de `on_click` evita lógica condicional
- Libera corretamente o recurso quando o usuário desejar

---

## Boas práticas gerais

- Use `key` sempre que widgets puderem se repetir
- Use `cache_data` para funções puras e custosas
- Use `cache_resource` para objetos vivos e reutilizáveis
- Evite misturar lógica de negócio dentro de widgets
- Lembre-se: cache **não elimina reexecução**, apenas otimiza
