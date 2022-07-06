from app.model.model_task import find_all_task, find_one_task, create_task
from app.model.model_task import delete_task, update_task
from .mock import mocks


def test_model_find_all_task():
    result = find_all_task(mocks)
    assert result == mocks.find()


def test_model_find_one_task():
    id = 1
    result = find_one_task(mocks, id)
    assert result == mocks.find_one(id)


def test_model_create_task():
    result = create_task(mocks, {})
    assert result == mocks.insert_one({})


def test_model_update_task():
    id = 1
    result = update_task(mocks, id, {})
    assert result == mocks.find_one_and_update(id, {})


def test_model_delete_task():
    id = 1
    result = delete_task(mocks, id)
    assert result == mocks.find_one_and_delete(id)
