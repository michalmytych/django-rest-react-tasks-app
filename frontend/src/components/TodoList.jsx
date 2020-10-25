import React, { Component, Fragment }  from 'react';
import { BrowserRouter as Router, Route, Link,} from "react-router-dom";
import TodoForm from './TodoForm';
import Filter from './Filter';
import Sort from './Sort';
import Task from './Task';
import Delete from './Delete';

  

class TodoList extends Component {
    state = {
        todos: [],
        logged_in: this.props.logged_in,
        instance: {},
        todos_filter: 1,
        todos_sort_order: 2,
        deleting: false,
        deleting_instance_id: 0
    };

    fetchToDos = () => {
        fetch('http://localhost:8000/todo/todos/', {
            headers: { Authorization: `JWT ${localStorage.getItem('token')}`}
        })
        .then(this.props.handleFetchErrors)
        .then(response => response.json() )
        .then(json => {
            this.setState({ 
                todos: json 
            });
        })
        .catch(error => {
            console.log(error);
        });
    }

    filterTodos = (todo, filter) => {
        switch (parseInt(filter, 10)) {
            case 1:
                return true; 
            case 2:
                return todo.done;
            case 3:
                return !todo.done;
            default:
                return true; 
        }
    }

    sortTodos = (previous, next, order) => {
        switch (parseInt(order, 10)){
            case 1:
                return Date.parse(previous.created_at) - Date.parse(next.created_at)
            case 2:
                return Date.parse(next.created_at) - Date.parse(previous.created_at)
            default:
                return true
        }
    }

    handleDelClick = (instance_id) => {
        this.setState({
            deleting_instance_id: instance_id,
            deleting: true
        });
    }

    handleDeleteView = () => {
        this.setState({
            deleting_instance_id: 0,
            deleting: false
        })
        this.fetchToDos();
    }

    componentDidMount() {
        this.fetchToDos();
    }

    render () {
        return (
            <section>
                {
                    this.state.deleting ?
                    <Delete
                        setState={p=>{this.setState(p)}}
                        instance_id={this.state.deleting_instance_id}
                        handleDeleteView={this.handleDeleteView}/>
                    :
                    null
                }


                <h1>To-Do List</h1>
                <Router>
                    <Route path={"/new"}>
                        <TodoForm 
                            todos={this.state.todos}
                            fetchToDos={this.fetchToDos}/>
                    </Route>

                    <Route path={"/edit/:todoId"}>
                        <TodoForm 
                            todos={this.state.todos}
                            fetchToDos={this.fetchToDos}/>
                    </Route>

                    <Route path="/">
                        <ul>
                            <li>
                                <Link
                                    className="btn" 
                                    to="/new">Dodaj</Link>
                            </li>
                            <li>
                                <Filter setState={p=>{this.setState(p)}} />
                            </li>                                
                            <li>
                                <Sort setState={p=>{this.setState(p)}} />
                            </li>
                            </ul>
                        <ul>
                            {
                               this.state.todos.length === 0 ?
                            <h2>Brak rzeczy do zrobienia.</h2>
                             :
                             this.state.todos
                             .filter((todo) => this.filterTodos(todo, this.state.todos_filter))
                             .sort((a,b) => this.sortTodos(a,b,this.state.todos_sort_order))
                            .map(todo => (
                                <li 
                                    className="todo-task-box"
                                    key={todo.id}>
                                    <Task 
                                        todo={todo}
                                        fetchToDos={this.fetchToDos}/>
                                    <Link 
                                        className="btn"
                                        to={`/edit/${todo.id}`}>Edytuj</Link>
                                    <button
                                        className="btn"
                                        onClick={() => this.handleDelClick(todo.id)}>
                                        Usuń
                                    </button>
                                </li>
                              ))
                              }
                        </ ul>
                    </Route>

                </Router>
            </section>
        )
    }
}


export default TodoList;