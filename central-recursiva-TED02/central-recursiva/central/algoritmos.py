def mdc(a, b):
    """Calcula recursivamente o MDC pelo algoritmo de Euclides."""
    if b == 0:
        return a
    return mdc(b, a % b)


def soma_digitos(n):
    """Calcula recursivamente a soma dos dígitos de um inteiro não negativo."""
    if n == 0:
        return 0
    return (n % 10) + soma_digitos(n // 10)
