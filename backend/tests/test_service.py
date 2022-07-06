import pytest
from app.service.service_task import find_all_task, create_task, update_task, delete_task
from .mock import mocks, mocks_service, mocks_service_fail


def test_service_find_all_task():
    result = find_all_task(mocks_service, mocks)
    assert result == mocks_service.find_all_task(mocks)


def test_service_create_task_fail():
    with pytest.raises(ValueError):
        description = 'Teste'
        task = 'Teste'
        status = ''
        create_task(mocks_service, mocks, description, task, status)

    with pytest.raises(ValueError):
        description = 'Teste'
        task = ''
        status = 'Teste'
        create_task(mocks_service, mocks, description, task, status)

    with pytest.raises(ValueError):
        description = ''
        task = 'Teste'
        status = 'Teste'
        create_task(mocks_service, mocks, description, task, status)


def test_service_create_task():
    description = 'Teste'
    task = 'Teste'
    status = 'Teste'
    result = create_task(mocks_service, mocks, description, task, status)
    assert result["_id"] == find_all_task(mocks_service, mocks)[0]["_id"] + 1


def test_service_update_task_fail():
    with pytest.raises(ValueError):
        id = 1,
        description = 'Teste'
        task = 'Teste'
        status = ''
        update_task(mocks_service, id, mocks, description, task, status)

    with pytest.raises(ValueError):
        id = 1,
        description = 'Teste'
        task = ''
        status = 'Teste'
        update_task(mocks_service, mocks, id, description, task, status)

    with pytest.raises(ValueError):
        id = 1,
        description = ''
        task = 'Teste'
        status = 'Teste'
        update_task(mocks_service, mocks, id, description, task, status)

    with pytest.raises(ValueError):
        description = 'Teste'
        task = 'Teste'
        status = 'Teste'
        update_task(mocks_service_fail, mocks, 1, description, task, status)


def test_service_update_task():
    description = 'Teste'
    task = 'Teste'
    status = 'Teste'
    result = update_task(mocks_service, mocks, 1, description, task, status)
    assert result["_id"] == 1


def test_service_delete_task_fail():
    with pytest.raises(ValueError):
        delete_task(mocks_service_fail, mocks, 1)


def test_service_delete_task():
    result = delete_task(mocks_service, mocks, 1)
    assert result