class Evento:
    def __init__(self, filas=5, colunas=10):
        self.filas = filas
        self.colunas = colunas
        self.mapa_assentos = [['O' for _ in range(colunas)] for _ in range(filas)]  # 'O' para disponível, 'X' para reservado

    def exibir_mapa(self):
        print("\nMapa de Assentos:")
        for i, linha in enumerate(self.mapa_assentos):
            print(" ".join(linha))
        print("\nLegenda: 'O' = Disponível | 'X' = Reservado\n")

    def reservar_assento(self, assento):
        linha, coluna = self._converter_assento(assento)
        if self.mapa_assentos[linha][coluna] == 'X':
            print(f"Assento {assento} já está reservado.")
        else:
            self.mapa_assentos[linha][coluna] = 'X'
            print(f"Assento {assento} reservado com sucesso.")

    def cancelar_reserva(self, assento):
        linha, coluna = self._converter_assento(assento)
        if self.mapa_assentos[linha][coluna] == 'O':
            print(f"O assento {assento} já está disponível.")
        else:
            self.mapa_assentos[linha][coluna] = 'O'
            print(f"Reserva do assento {assento} cancelada com sucesso.")

    def _converter_assento(self, assento):
        try:
            linha = ord(assento[0].upper()) - 65
            coluna = int(assento[1:]) - 1
            if linha < 0 or linha >= self.filas or coluna < 0 or coluna >= self.colunas:
                raise ValueError
            return linha, coluna
        except (IndexError, ValueError):
            raise ValueError("Formato de assento inválido. Use, por exemplo, A1, B3, etc.")

def menu():
    evento = Evento()
    while True:
        print("1. Visualizar mapa de assentos")
        print("2. Reservar assento")
        print("3. Cancelar reserva")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                evento.exibir_mapa()
            elif opcao == '2':
                assento = input("Digite o assento para reservar (ex: A1): ")
                evento.reservar_assento(assento)
            elif opcao == '3':
                assento = input("Digite o assento para cancelar (ex: A1): ")
                evento.cancelar_reserva(assento)
            elif opcao == '4':
                print("Encerrando o sistema.")
                break
            else:
                print("Opção inválida.")
        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    menu()
