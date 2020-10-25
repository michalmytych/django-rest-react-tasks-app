import React, { Component } from 'react'
import Nav from './components/Nav';
import LoginForm from './components/Login';
import SignupForm from './components/SignUp';
import Guest from './components/Guest';
import TodoList from './components/TodoList';



export default class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            logged_in: localStorage.getItem('token') ? true : false,
            username: '',
            displayed_form: '',
            form_is_displayed: false
        };
        
    }

    handleFetchErrors = (response) => {
        if (!response.ok) {
            throw Error(response.statusText);
        }
        return response;
    }

    componentDidMount() {
        if (this.state.logged_in) {
            fetch('http://localhost:8000/todo/current_user/', {
              headers: {
                Authorization: `JWT ${localStorage.getItem('token')}`
              }
            })
            .then(this.handleFetchErrors)
            .then(response => response.json() )
            .then(json => {
                this.setState({ username: json.username });
            })
            .catch(error => console.log(error) );
          }
    }

    handle_login = (event, data) => {
        event.preventDefault();
        fetch('http://localhost:8000/token-auth/', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(this.handleFetchErrors)
        .then(response => response.json() )
        .then(json => {
            localStorage.setItem('token', json.token);
            this.setState({
                logged_in: true,
                displayed_form: '',
                username: json.user.username
            });
        })
        .catch(error => {
            alert("Error while: handle_login()");
            console.log(error);
        });
    };

    handle_signup = (event, data) => {
        event.preventDefault();
        fetch('http://localhost:8000/todo/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(this.handleFetchErrors)
        .then(response => response.json() )
        .then(json => {
            localStorage.setItem('token', json.token);
            this.setState({
                logged_in: true,
                displayed_form: '',
                username: json.username
            });
        })
        .catch(error => {
            alert("Error while: handle_signup()");
            console.log(error);
        });
    };

    handle_logout = () => {
        localStorage.removeItem('token');
        this.setState({ 
            logged_in: false, 
            username: '',
        });
    };

    display_form = form => {
        this.setState({
            form_is_displayed: true,
            displayed_form: form
        });
    };

    render() {
        let form;
        switch (this.state.displayed_form) {
            case 'login':
                form = <LoginForm 
                            setParentState={(p) => this.setState(p)}
                            handle_login={this.handle_login} />;
                break;
            case 'signup':
                form = <SignupForm 
                            setParentState={(p) => this.setState(p)}
                            handle_signup={this.handle_signup} />;
                break;
            default:
                form = null;
        }
    
        return (
          <div className="page-content">
            <div>
                <Nav
                    logged_in={this.state.logged_in}
                    display_form={this.display_form}
                    handle_logout={this.handle_logout}
                />
            </div>
            {
            this.state.form_is_displayed ?
            form
            :
            null}
            {this.state.logged_in ? 
            <main>
                <TodoList 
                    logged_in={this.state.logged_in} 
                    handleFetchErrors={this.handleFetchErrors} 
                    logout={this.handle_logout}
                /> 
            </main>
            : 
            <Guest />
            }
          </div>
        );
      }
    }
