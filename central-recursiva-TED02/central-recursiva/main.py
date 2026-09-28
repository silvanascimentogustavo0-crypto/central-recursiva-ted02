from central.algoritmos import mdc, soma_digitos
from central.validacoes import validar_mdc, validar_soma
from central.excecoes import EntradaInvalidaError, OperacaoInvalidaError


def processar(entrada):
    dados = entrada.split()

    if not dados:
        raise OperacaoInvalidaError

    operacao = dados[0]

    if operacao == "M":
        if len(dados) != 3:
            raise EntradaInvalidaError

        try:
            a = int(dados[1])
            b = int(dados[2])
        except ValueError:
            raise EntradaInvalidaError

        validar_mdc(a, b)
        return f"MDC = {mdc(a, b)}"

    elif operacao == "S":
        if len(dados) != 2:
            raise EntradaInvalidaError

        try:
            n = int(dados[1])
        except ValueError:
            raise EntradaInvalidaError

        validar_soma(n)
        return f"SOMA = {soma_digitos(n)}"

    else:
        raise OperacaoInvalidaError


def main():
    q = int(input())

    for _ in range(q):
        try:
            entrada = input()
            resultado = processar(entrada)
            print(resultado)

        except EntradaInvalidaError:
            print("ERRO: EntradaInvalida")

        except OperacaoInvalidaError:
            print("ERRO: OperacaoInvalida")

        finally:
            # O bloco finally é executado independentemente de ocorrer exceção.
            # Não há saída aqui para preservar o formato exigido pelo problema.
            pass


if __name__ == "__main__":
    main()
