import React, {Component, Fragment} from 'react';
import { withRouter } from "react-router-dom";



class TodoForm extends Component {
    state = {
        name: '',
        description: '',
        deadline: ''
    }

    handle_change = (event) => {
        const name = event.target.name;
        const value = event.target.value;
    
        this.setState(prevstate => {
            const newState = { ...prevstate };
            newState[name] = value;
            return newState;
        });
    };

    componentDidMount() {
        if (this.props.match.params.todoId) {

            let instance = this.props.todos.find(
                todo => todo.id === parseInt(this.props.match.params.todoId, 10)
            )

            this.setState({
                name: instance.name,
                description: instance.description,
                deadline: instance.deadline,
            });
        }
    }

    exitForm = () => {
        this.setState({
            name: '',
            description: '',
            deadline: ''
        });
    
        this.props.history.push("/");
        this.props.fetchToDos();
    }

    handle_submit = (e, data) => {
        let todo = {
            name: data.name,
            description: data.description,
            deadline: data.deadline,
            done: false,
            created_at: "",
            user: null
        }

        if (todo.name.length === 0 || todo.description.length === 0 || todo.name.length === 0){
            alert("Formularz został niepoprawnie wypełniony. Nie zapisano żadnych zmian.");
            this.exitForm();
        }

        if (this.props.match.params.todoId) {
            /*
                EDITING EXISTING TASK INSTANCE WITH PATCH
            */
            e.preventDefault();
            fetch(`http://localhost:8000/todo/todos/${this.props.match.params.todoId}/`, {
                method: 'PATCH',
                headers: {
                'Content-Type': 'application/json',
                    Authorization: `JWT ${localStorage.getItem('token')}`
                },
                body: JSON.stringify({
                    name: todo.name,
                    description: todo.description,
                    deadline: todo.deadline
                })
            })
            .then(this.props.handleFetchErrors)
            .then(                
                this.props.fetchToDos()
            )
            .catch(error => {
                console.log(error);
            });
        }
        else{
            /*
                CREATING NEW TASK WITH POST
            */
            e.preventDefault();
            fetch('http://localhost:8000/todo/todos/', {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json',
                    Authorization: `JWT ${localStorage.getItem('token')}`
                },
                body: JSON.stringify(todo)
            })
            .then(this.props.handleFetchErrors)
            .then(                
                this.props.fetchToDos()
            )
            .catch(error => {
                console.log(error);
            });
        }
    
        this.exitForm();
    };

    render() {
        return (
            <Fragment>
                <div
                    onClick={this.exitForm} 
                    className="blurred-bg"></div>
                <div className="overlay-box">
                    <form onSubmit={event => this.handle_submit(event, this.state)}>
                        <button 
                            className="btn"
                            onClick={this.exitForm}>Wróć</button>
                        <h4>Dodaj nową rzecz do zrobienia:</h4>
                        <label htmlFor="name">Tytuł:</label>
                        <input
                            type="text"
                            name="name"
                            value={this.state.name}
                            onChange={this.handle_change}/>
                        <label htmlFor="description">Opis:</label>
                        <textarea
                            type="text"
                            name="description"
                            value={this.state.description}
                            onChange={this.handle_change}/>
                        <label htmlFor="deadline">Deadline:</label>
                        <input 
                            type="datetime-local"                
                            name="deadline"
                            onChange={this.handle_change}>                      
                        </input>
                        <input 
                            className="btn"
                            type="submit"
                            value={
                                this.props.match.params.todoId ?
                                "Zapisz"
                                :
                                "Dodaj"
                            }/>
                    </form>
                </div>
            </Fragment>
        );
    }
}


export default withRouter(TodoForm);
