try:
    1 / 0
except Exception as err:
    # Tratamento caso no bloco do try acontece alguma exceção
    # Outros tipos de exceções: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
    print("Divisão por zero")
    exit(1)
