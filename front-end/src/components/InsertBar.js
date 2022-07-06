import React, { useState, useContext } from "react";
import ToDoListContext from '../context/ToDoListContext';
import { fetchFindAll, fetchCreate } from "../services/fetchApi";

function InsertBar() {
  const { setData, isEditItem } = useContext(ToDoListContext);
  const [task, setTask] = useState('');
  const [responsible, setResponsible] = useState('');

  async function addList() {
    await fetchCreate({ task, responsible, status: 'Pendente' });
    await fetchFindAll(setData);
    setTask('');
    setResponsible('');
  }

  return (
    <div>
      <div className="input-group mt-5">
        <input
          className="form-control"
          type="text" placeholder="Tarefa"
          value={ task }
          onChange={ ({ target }) => setTask(target.value)}
          data-testid="input-task"
        />
        <input
          className="form-control"
          type="text"
          value={ responsible }
          placeholder="Responsável"
          onChange={ ({ target }) => setResponsible(target.value)}
          data-testid="input-responsible"
        />
      </div>
      <div className="mt-2 col-lg-12 rigth">
        <button
          className="btn btn-primary"
          type="button"
          onClick={ () => addList()}
          disabled={ isEditItem.edited }
        >
          ADICIONAR
        </button>
      </div>      
    </div>
  );
}

export default InsertBar;
