class IHM:

    def __init__(self):
        print("IHM initialized")

    def is_alive(self):
        """Verifica se o sistema está ativo."""

        return True

    def modelo(self):
        """Retorna o modelo do sistema."""

        return "SF800Q+"

    def continue_apos_excesao(self):
        """Determina se deve continuar após uma exceção."""

        return True

    def result(self, message):
        """Exibe o resultado passado."""

        print(f"Result: {message}")

    def erro(self, message):
        """Exibe a mensagem de erro passada."""

        print(f"Erro: {message}")

    def limite_ultrapassado(self, message):
        """Exibe uma mensagem quando o limite é ultrapassado."""

        print(f"Limite Ultrapassado: {message}")

