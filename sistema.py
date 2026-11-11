class Equipamento:
    def __init__(self, codigo, nome, quantidade):
        if codigo is None or str(codigo).strip() == "":
            raise ValueError("Código do equipamento não pode ser vazio.")
        if nome is None or str(nome).strip() == "":
            raise ValueError("Nome do equipamento não pode ser vazio.")
        if isinstance(quantidade, bool) or not isinstance(quantidade, int):
            raise ValueError("Quantidade deve ser um número inteiro.")
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")

        self.codigo = codigo
        self.nome = str(nome).strip()
        self.quantidade = quantidade


estoque = []


def cadastrar_equipamento(codigo, nome, quantidade):
    if any(equipamento.codigo == codigo for equipamento in estoque):
        raise ValueError(f"Código {codigo} já cadastrado.")

    equipamento = Equipamento(codigo, nome, quantidade)
    estoque.append(equipamento)
    return equipamento


def emprestar_equipamento(codigo):
    for equipamento in estoque:
        if equipamento.codigo == codigo:
            if equipamento.quantidade > 0:
                equipamento.quantidade -= 1
                return True
            return False
    return False


def devolver_equipamento(codigo):
    for equipamento in estoque:
        if equipamento.codigo == codigo:
            equipamento.quantidade += 1
            return True
    return False


def consultar_quantidade(codigo):
    for equipamento in estoque:
        if equipamento.codigo == codigo:
            return equipamento.quantidade
    return None


def gerar_relatorio():
    if not estoque:
        return "Nenhum equipamento cadastrado."

    return "\n".join(f"{equipamento.nome}: {equipamento.quantidade}" for equipamento in estoque)