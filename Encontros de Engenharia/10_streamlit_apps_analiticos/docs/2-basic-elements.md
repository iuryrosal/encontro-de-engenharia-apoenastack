# Streamlit – Elementos de Interface e Interação

Nesta seção, exploramos os **principais elementos visuais e interativos do Streamlit**, entendendo não apenas *como usá-los*, mas também *qual o papel conceitual de cada grupo* dentro da construção de uma aplicação web reativa.

---

## Text Elements

Os **Text Elements** são responsáveis por estruturar e comunicar informação textual ao usuário. Eles funcionam como a base semântica da interface, organizando o conteúdo em níveis hierárquicos semelhantes ao HTML.

```python
st.title("Esse é um título principal")
st.header("Um tópico aqui")
st.subheader("Um subtópico por aqui!")
st.markdown("Estrutura __de__ **markdown**!")
st.caption("small text")
```

### Conceitos importantes

- `st.title`, `st.header` e `st.subheader` criam uma **hierarquia visual**, facilitando a leitura e a navegação.
- `st.markdown` permite escrever textos ricos usando **Markdown**, ideal para documentação, descrições e explicações.
- `st.caption` é usado para textos auxiliares, observações ou legendas.

---

## Exibição de Código

```python
code = """
print('Hello World')
"""

st.code(code, language="python")
```

O `st.code` é especialmente útil para:
- Demonstrações didáticas
- Exibição de exemplos
- Documentação técnica dentro da aplicação

Ele aplica **syntax highlighting** de acordo com a linguagem informada.

---

## Elementos Visuais Auxiliares

```python
st.divider()
st.metric(label="Clientes", value=100000)
```

- `st.divider()` cria uma separação visual entre blocos da interface.
- `st.metric()` é usado para exibir **KPIs**, métricas ou indicadores de forma destacada, muito comum em dashboards analíticos.

---

## Inserindo Imagens

```python
import os

st.image(os.path.join(os.getcwd(), "static", "BG.jpg"))
```

O `st.image` permite renderizar imagens locais ou via URL.  
Esse recurso é amplamente utilizado para:
- Logos
- Backgrounds
- Visualizações estáticas
- Ilustrações explicativas

---

## Data Elements

Os **Data Elements** são voltados para exibição e interação com dados estruturados, principalmente usando **Pandas DataFrames**.

```python
df = pd.DataFrame(
    {
        "name": ["Iury", "Fernando", "Paulo", "Dudu"],
        "Age": [25, 30, 28, 18]
    }
)

st.dataframe(df)
st.data_editor(df)
st.table(df)
```

- `st.dataframe`  
  - Tabela interativa  
  - Suporta scroll, ordenação e zoom  

- `st.data_editor`  
  - Permite **edição direta dos dados pelo usuário**  
  - Muito útil para inputs tabulares  

- `st.table`  
  - Renderização estática  
  - Ideal para pequenos conjuntos de dados  

---

## Chart Elements

O Streamlit oferece gráficos de alto nível que abstraem bibliotecas como **Altair** e **Vega-Lite**, além de integração com **Matplotlib**.

```python
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# Gráfico de Área
st.area_chart(data)

# Gráfico de Barra
st.bar_chart(data)

# Gráfico de Linha
st.line_chart(data)
```

Esses gráficos são ideais para **prototipação rápida**, pois exigem configuração mínima.


### Gráfico de Dispersão

```python
data_points = pd.DataFrame(
    {
        "x": np.random.randn(100),
        "y": np.random.randn(100)
    }
)

st.scatter_chart(data_points)
```

Muito utilizado para:
- Análise exploratória
- Correlação entre variáveis
- Identificação de padrões ou outliers

---

### Mapas

```python
map_data = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"]
)

st.map(map_data)
```

O `st.map` abstrai bibliotecas de mapas e permite visualizações geoespaciais rápidas, desde que o DataFrame possua colunas `lat` e `lon`.

---

### Integração com Matplotlib

```python
fig, ax = plt.subplots()
ax.plot(data["A"], label="A")
ax.plot(data["B"], label="B")
ax.plot(data["C"], label="C")
ax.set_title("Pyplot Line Chart")
ax.legend()

st.pyplot(fig)
```

Esse recurso é essencial quando:
- Precisamos de **controle total sobre o gráfico**
- Já possuímos visualizações legadas em Matplotlib
- Trabalhamos com gráficos científicos mais complexos

---

## Form Elements

Os **Form Elements** são utilizados para coletar múltiplas entradas do usuário de forma controlada.

Um conceito-chave é o uso de **`st.form`**, que evita múltiplas reexecuções do script enquanto o usuário preenche os campos.

```python
form_answer = {}

with st.form(key="sample_form"):
    form_answer["name"] = st.text_input("Seu nome")
    form_answer["age"] = st.number_input("Sua idade")
    form_answer["feedback"] = st.text_area("Depoimento")
    form_answer["birth_date"] = st.date_input("Data de Nascimento")
    form_answer["time"] = st.time_input("Horário de Preferência")
    form_answer["choice"] = st.radio("Escolha a melhor opção", ["Manhã", "Tarde", "Noite"])
    form_answer["gender"] = st.selectbox("Gênero", ["Masculino", "Feminino", "Outro"])
    form_answer["slider_value"] = st.select_slider("Sua Avaliação", options=[1, 2, 3, 4, 5])
    form_answer["notifications"] = st.checkbox("Receber atualizações?")

    submit_form = st.form_submit_form(label="Enviar")

    if submit_form:
        if not all(form_answer.values()):
            st.warning("Preencha todos os campos")
        else:
            st.balloons()
            st.write("### Info")
            for key, value in form_answer.items():
                st.write(f"{key}: {value}")
```
