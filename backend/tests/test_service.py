import pytest
from app.service.service_task import find_all_task, create_task
from .mock import mocks
from .mock import mocks_service


def test_service_find_all_task():
    result = find_all_task(mocks_service, mocks)
    assert result == mocks_service.find_all_task(mocks)


def test_service_create_task_fail():
    with pytest.raises(ValueError):
        responsible = 'Teste'
        task = 'Teste'
        status = ''
        create_task(mocks_service, mocks, responsible, task, status)

    with pytest.raises(ValueError):
        responsible = 'Teste'
        task = ''
        status = 'Teste'
        create_task(mocks_service, mocks, responsible, task, status)

    with pytest.raises(ValueError):
        responsible = ''
        task = 'Teste'
        status = 'Teste'
        create_task(mocks_service, mocks, responsible, task, status)


def test_service_create_task():
    responsible = 'Teste'
    task = 'Teste'
    status = 'Teste'
    result = create_task(mocks_service, mocks, responsible, task, status)
    assert result["_id"] == find_all_task(mocks_service, mocks)[0]["_id"] + 1
