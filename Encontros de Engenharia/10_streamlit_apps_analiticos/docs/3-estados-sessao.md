# Session State no Streamlit

Um dos comportamentos mais importantes (e confusos no início) do Streamlit é o seu **modelo de execução reativo**.

Sempre que um botão é clicado, um input é alterado ou um código é modificado, **todo o script Python é reexecutado do início ao fim**.

---

## O problema do estado em variáveis comuns

Considere o seguinte exemplo:

```python
counter = 0

st.write(f"Counter Value: {counter}")

if st.button("Increment Counter"):
    counter += 1
    st.write(f"New Counter Value: {counter}")
else:
    st.write("Counter not incremented")
```

O que acontece aqui?

- A variável `counter` é inicializada com valor `0`
- Ao clicar no botão:
  - O Streamlit **reexecuta o script inteiro**
  - O botão retorna `True`
  - O contador é incrementado para `1`
- Porém, na próxima interação:
  - O script é executado novamente
  - `counter` volta a ser inicializado como `0`
  - O valor exibido será sempre `1`

Ou seja, **variáveis Python tradicionais não persistem estado entre reexecuções**.

---

## Por que isso acontece?

Isso ocorre porque:
- O Streamlit **não mantém o estado das variáveis locais**
- Cada execução é stateless por padrão
- O botão apenas sinaliza um evento (`True` naquele ciclo de execução)

Esse modelo é excelente para simplicidade e previsibilidade, mas exige um mecanismo explícito para persistência de estado.

---

## A solução: Session State

O **Session State** (`st.session_state`) é um objeto fornecido pelo Streamlit para armazenar **valores persistentes dentro de uma sessão de usuário**.

### Conceito de sessão

- Cada usuário que abre a aplicação no navegador recebe uma **sessão própria**
- A sessão:
  - É criada quando a página é aberta
  - Permanece ativa enquanto o usuário não recarregar manualmente ou fechar a aba
- As reexecuções automáticas do Streamlit **não reinicializam o session state**

Ou seja, os valores armazenados no `st.session_state` **sobrevivem às reexecuções do script**.

---

## Implementando o contador corretamente

```python
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.write(f"Old Counter Value: {st.session_state.counter}")

if st.button("Increment Counter"):
    st.session_state.counter += 1

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f"Current Counter Value: {st.session_state.counter}")
```

O que está acontecendo aqui?

1. **Inicialização segura**
   ```python
   if "counter" not in st.session_state:
       st.session_state.counter = 0
   ```
   - Garante que o contador seja criado apenas uma vez por sessão

2. **Leitura do estado persistente**
   ```python
   st.write(st.session_state.counter)
   ```
   - O valor não é perdido entre reexecuções

3. **Atualização baseada em eventos**
   ```python
   if st.button("Increment Counter"):
       st.session_state.counter += 1
   ```
   - O botão apenas dispara a lógica
   - O estado fica salvo no objeto da sessão

4. **Reset controlado**
   ```python
   if st.button("Reset"):
       st.session_state.counter = 0
   ```
