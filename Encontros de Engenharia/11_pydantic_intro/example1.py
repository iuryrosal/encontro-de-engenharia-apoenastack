from pydantic import validate_call, ValidationError
# Explorar a dor que o Pydantic

# Problema: a="a", b=1
def soma(a: int, b: int):
    return a + b

# Solução do Problema
@validate_call
def soma_corrigida(a: int, b: int):
    return a + b

try:
    soma_corrigida("a", 1)
except ValidationError as e:
    print("Falha na entrada: ", str([error.get("msg") for error in e.errors()]))