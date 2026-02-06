# Streamlit – Layout e Organização da Interface

Nesta seção, abordamos os principais **componentes de layout do Streamlit**, responsáveis por organizar visualmente a aplicação e estruturar a experiência do usuário.

Diferente de frameworks web tradicionais, o Streamlit oferece uma **API declarativa**, onde o layout é definido diretamente no fluxo do código Python.

---

## Sidebar (Barra Lateral)

A **Sidebar** é uma área fixa no lado esquerdo da aplicação, geralmente utilizada para:
- Navegação
- Filtros
- Configurações globais
- Inputs que afetam toda a aplicação

```python
import streamlit as st

st.sidebar.title("Título da Sidebar")
st.sidebar.write("Qualquer coisa aqui")
```

- Tudo que é renderizado via `st.sidebar` aparece automaticamente na barra lateral
- Ideal para controles que não fazem parte do conteúdo principal
- Ajuda a manter a interface principal mais limpa e focada

---

## Tabs (Abas)

As **Tabs** permitem dividir o conteúdo da aplicação em múltiplas seções, exibidas uma de cada vez.

```python
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Tab1")

with tab2:
    st.write("Tab2")

with tab3:
    st.write("Tab3")
```

- Cada aba funciona como um **contexto de renderização**
- O conteúdo de uma aba só é exibido quando ela está ativa
- O script continua sendo reexecutado normalmente, independentemente da aba selecionada

As tabs são ideais para:
- Separar análises
- Criar dashboards multi-visão
- Organizar grandes volumes de conteúdo

---

## Columns (Colunas)

As **Columns** permitem criar layouts horizontais, dividindo a tela em múltiplas colunas.

```python
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")

with col2:
    st.header("Column 2")
```

### Conceitos importantes

- As colunas seguem um sistema de grid simples
- O conteúdo dentro de cada coluna é empilhado verticalmente
- Também é possível definir larguras relativas, por exemplo:
  ```python
  st.columns([1, 2, 1])
  ```

Uso comum:
- Dashboards
- Comparações lado a lado
- Organização de métricas e gráficos

---

## Expander

O **Expander** cria uma área colapsável, exibida apenas quando o usuário decide expandi-la.

```python
with st.expander("Expand"):
    st.write("Isso tava escondido...")
```

## Páginas Múltiplas no Streamlit

Além de Tabs, o Streamlit permite criar **aplicações multipágina reais**, onde cada página possui:
- Seu próprio script Python
- Seu próprio layout
- Sua própria lógica

Esse modelo é ideal para aplicações maiores e mais organizadas.

O Streamlit reconhece automaticamente páginas quando utilizamos a pasta especial chamada **`pages/`**.

Exemplo de estrutura:

```
project/
│
├── main.py
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Análises.py
│   └── 3_Configurações.py
```

- `main.py` é a **página principal**
- Cada arquivo dentro de `pages/` vira uma **página navegável**
- A navegação aparece automaticamente na Sidebar
- O prefixo numérico define a **ordem das páginas**


**Exemplo de Página (`pages/1_Dashboard.py`)**

```python
import streamlit as st

st.title("Dashboard")
st.write("Conteúdo do Dashboard")
```

Cada página:
- É um script independente
- Compartilha o mesmo `st.session_state`
- Pode acessar dados globais da aplicação


A navegação entre páginas:
- É gerenciada automaticamente pelo Streamlit
- Aparece na Sidebar
- Não exige código adicional

O Streamlit cuida internamente do roteamento.

### Integração com Session State

Um ponto importante:

- O `st.session_state` é **compartilhado entre todas as páginas**
- Isso permite:
  - Login em uma página
  - Uso de permissões em outra
  - Compartilhamento de filtros globais

Exemplo:

```python
if "user" not in st.session_state:
    st.session_state.user = None
```

Esse valor estará disponível em qualquer página da aplicação.