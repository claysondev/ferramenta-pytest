import pytest

from sistema import *


def setup_function():
    estoque.clear()

def test_cadastro():
    cadastrar_equipamento(1, "Notebook", 5)
    assert len(estoque) == 1
    assert estoque[0].codigo == 1
    assert estoque[0].nome == "Notebook"
    assert estoque[0].quantidade == 5


def test_emprestimo_com_sucesso():
    cadastrar_equipamento(1, "Notebook", 5)
    assert emprestar_equipamento(1) == True
    assert consultar_quantidade(1) == 4


def test_emprestimo_estoque_zerado():
    cadastrar_equipamento(1, "Notebook", 0)
    assert emprestar_equipamento(1) == False
    assert consultar_quantidade(1) == 0


def test_emprestimo_codigo_inexistente():
    assert emprestar_equipamento(99) == False


def test_devolucao_com_sucesso():
    cadastrar_equipamento(1, "Notebook", 5)
    assert devolver_equipamento(1) == True
    assert consultar_quantidade(1) == 6


def test_devolucao_codigo_inexistente():
    assert devolver_equipamento(99) == False


def test_consulta_quantidade():
    cadastrar_equipamento(1, "Notebook", 5)
    assert consultar_quantidade(1) == 5


def test_consulta_codigo_inexistente():
    assert consultar_quantidade(99) is None


def test_emprestimo_ate_zerar_estoque():
    cadastrar_equipamento(1, "Mouse", 2)
    assert emprestar_equipamento(1) == True
    assert emprestar_equipamento(1) == True
    assert consultar_quantidade(1) == 0
    assert emprestar_equipamento(1) == False


def test_devolucao_apos_estoque_zerado():
    cadastrar_equipamento(1, "Mouse", 1)
    emprestar_equipamento(1)
    assert consultar_quantidade(1) == 0
    assert devolver_equipamento(1) == True
    assert consultar_quantidade(1) == 1


def test_multiplos_equipamentos_independentes():
    cadastrar_equipamento(1, "Notebook", 5)
    cadastrar_equipamento(2, "Mouse", 10)
    emprestar_equipamento(1)
    assert consultar_quantidade(1) == 4
    assert consultar_quantidade(2) == 10

def test_impede_codigo_duplicado():
    cadastrar_equipamento(1, "Notebook", 5)
    with pytest.raises(ValueError):
        cadastrar_equipamento(1, "Mouse", 3)
    assert len(estoque) == 1


def test_impede_quantidade_negativa():
    with pytest.raises(ValueError):
        cadastrar_equipamento(1, "Notebook", -5)
    assert len(estoque) == 0


def test_impede_nome_vazio():
    with pytest.raises(ValueError):
        cadastrar_equipamento(1, "", 5)
    assert len(estoque) == 0


def test_impede_codigo_vazio():
    with pytest.raises(ValueError):
        cadastrar_equipamento("", "Notebook", 5)
    assert len(estoque) == 0


def test_relatorio_equipamentos_cadastrados():
    cadastrar_equipamento(1, "Notebook", 5)
    cadastrar_equipamento(2, "Mouse", 10)
    relatorio = gerar_relatorio()
    assert "Notebook" in relatorio
    assert "Mouse" in relatorio


def test_impede_codigo_so_espacos():
    with pytest.raises(ValueError):
        cadastrar_equipamento("   ", "Notebook", 5)
    assert len(estoque) == 0


def test_impede_nome_so_espacos():
    with pytest.raises(ValueError):
        cadastrar_equipamento(1, "   ", 5)
    assert len(estoque) == 0


def test_impede_quantidade_booleana():
    with pytest.raises(ValueError):
        cadastrar_equipamento(1, "Notebook", True)
    with pytest.raises(ValueError):
        cadastrar_equipamento(2, "Mouse", False)
    assert len(estoque) == 0


def test_impede_quantidade_nao_inteira():
    with pytest.raises(ValueError):
        cadastrar_equipamento(1, "Notebook", "5")
    with pytest.raises(ValueError):
        cadastrar_equipamento(2, "Mouse", 2.5)
    assert len(estoque) == 0

def test_relatorio_estoque_vazio():
    assert gerar_relatorio() == "Nenhum equipamento cadastrado."