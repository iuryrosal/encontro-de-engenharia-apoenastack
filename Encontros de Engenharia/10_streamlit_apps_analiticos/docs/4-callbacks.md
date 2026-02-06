# Callbacks no Streamlit

Os **callbacks** no Streamlit são mecanismos que permitem **executar funções automaticamente em resposta a eventos de interação do usuário**, como cliques em botões ou mudanças em inputs.

Eles ajudam a:
- Separar lógica de interface da lógica de negócio
- Evitar condicionais excessivas
- Tornar o código mais limpo, previsível e reutilizável

---

## O que é um Callback?

Um **callback** é uma função que:
- Não recebe argumentos diretamente do widget
- É executada automaticamente quando um evento ocorre
- Pode acessar e modificar o `st.session_state`

No Streamlit, callbacks são usados principalmente com:
- `on_click`
- `on_change`

---

## Callback com `on_click`

O uso mais comum de callbacks acontece com botões.

**Exemplo sem callback (padrão)**

```python
if st.button("Increment"):
    st.session_state.counter += 1
```

Esse padrão funciona, mas:
- Mistura evento com lógica
- Escala mal em aplicações grandes

**Exemplo com callback**

```python
def increment_counter():
    st.session_state.counter += 1

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.button("Increment", on_click=increment_counter)
st.write(st.session_state.counter)
```

O que está acontecendo?

- O botão apenas dispara o evento
- Toda a lógica está isolada na função `increment_counter`
- O estado é manipulado via `st.session_state`

---

## Callback com `on_change`

Callbacks também podem ser usados em inputs, executando uma função **sempre que o valor muda**.

**Exemplo com `text_input`**

```python
def on_name_change():
    st.session_state.name_upper = st.session_state.name.upper()

st.text_input(
    "Digite seu nome",
    key="name",
    on_change=on_name_change
)

st.write(st.session_state.get("name_upper", ""))
```

- `on_change` é disparado **imediatamente após a mudança**
- Não depende de botão
- Ideal para validações e transformações automáticas

---

## Passando argumentos para callbacks

Callbacks podem receber argumentos via `args` e `kwargs`.

```python
def update_value(step):
    st.session_state.counter += step

st.button(
    "Increment +2",
    on_click=update_value,
    args=(2,)
)
```

Isso permite reutilizar a mesma função para múltiplos widgets.

---

## Callbacks e Session State

Callbacks **sempre operam sobre o `st.session_state`**.

Boas práticas:
- Nunca depender de variáveis locais
- Sempre ler e escrever no estado da sessão
- Inicializar valores antes de usar

```python
if "value" not in st.session_state:
    st.session_state.value = 0
```

---

## Callback vs Condicional

**Sem callback**

```python
if st.button("Salvar"):
    salvar_dados()
```

**Com callback**

```python
st.button("Salvar", on_click=salvar_dados)
```

**Vantagens do callback**

- Código mais declarativo
- Menos `if`
- Melhor separação de responsabilidades
- Mais fácil de testar e manter

---

## Callbacks em Formulários

Dentro de `st.form`, callbacks **não são executados automaticamente** em cada widget.

O fluxo correto é:

```python
def submit_form():
    st.session_state.submitted = True

with st.form("my_form"):
    st.text_input("Nome", key="name")
    st.number_input("Idade", key="age")

    st.form_submit_button(
        "Enviar",
        on_click=submit_form
    )
```

Dentro de forms:
- O callback só executa no submit
- Inputs não disparam `on_change` individualmente

---

## Anti-padrões comuns

❌ Usar callbacks com variáveis locais  
❌ Criar efeitos colaterais fora do `session_state`  
❌ Lógica pesada diretamente no callback  
❌ Esquecer de inicializar estado  

---

## Boas práticas com callbacks

- Use callbacks para **eventos**
- Use `session_state` para **estado**
- Mantenha callbacks pequenos e objetivos
- Prefira callbacks a condicionais repetitivas
- Combine callbacks com `cache` quando necessário
