import pytest
from app.services import TodoService

def test_service_criar_tarefa(service):
    """
    Testa a criação de uma nova tarefa através do TodoService.
    """
    service = TodoService()
    task = service.create("algo" , "algo detalhado")

    assert task.title == "algo"
    assert task.description == "algo detalhado"


def test_service_listar_todas_as_tarefas(service):
    """
    Testa se o serviço lista corretamente todas as tarefas cadastradas.
    """
    service = TodoService()
    task = service.create("algo" , "algo detalhado")
    lista = service.list_all()
    assert lista[0].title == "algo"


def test_service_buscar_tarefa_por_id_existente(service):
    """
    Testa a busca de uma tarefa por ID quando ela existe no repositório.
    """
    service = TodoService()
    task = service.create("algo" , "algo detalhado")
    task2 = service.get_by_id(1)
    assert task2.title == "algo"


def test_service_buscar_tarefa_por_id_inexistente(service):
    """
    Testa a busca de uma tarefa por ID inexistente, esperando retorno None.
    """
    service = TodoService()
    task = service.create("algo" , "algo detalhado")
    task2 = service.get_by_id(0)
    assert task2 == none


def test_service_atualizar_tarefa_existente(service):
    """
    Testa a atualização de título, descrição e status de conclusão de uma tarefa.
    """
    
    pass


def test_service_remover_tarefa_existente(service):
    """
    Testa a remoção de uma tarefa existente e verifica se ela deixa de existir.
    """
    
    pass


def test_service_remover_tarefa_inexistente(service):
    """
    Testa a tentativa de remoção de ID inexistente, esperando retorno False.
    """
    
    pass
