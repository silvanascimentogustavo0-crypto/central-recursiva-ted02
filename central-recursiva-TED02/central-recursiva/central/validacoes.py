from central.excecoes import EntradaInvalidaError


def validar_mdc(a, b):
    """Valida os valores utilizados no cálculo do MDC."""
    if a <= 0 or b <= 0:
        raise EntradaInvalidaError


def validar_soma(n):
    """Valida o número utilizado na soma dos dígitos."""
    if n < 0:
        raise EntradaInvalidaError
