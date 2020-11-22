import React, { Fragment } from 'react';



export default class LoginForm extends React.Component {
  state = {
    username: '',
    password: ''
  };

  handle_change = e => {
    const name = e.target.name;
    const value = e.target.value;
    this.setState(prevstate => {
      const newState = { ...prevstate };
      newState[name] = value;
      return newState;
    });
  };

  handleFormQuit = () => {
    this.props.setParentState({
      form_is_displayed: false
    });
  }

  render() {
    return (
      <div className="auth-block container">
        <div
            onClick={this.handleFormQuit}></div>
        <div>
          <form 
            className="auth-form"
            onSubmit={e => this.props.handle_login(e, this.state)}>
            <h4>Logowanie</h4>
            <input
              className="auth-inpt text-inpt"
              type="text"
              name="username"
              value={this.state.username}
              onChange={this.handle_change}
            />
            <input
              className="auth-inpt text-inpt"
              type="password"
              name="password"
              value={this.state.password}
              onChange={this.handle_change}
            />
            <input 
              className="auth-inpt basic-btn login-btn"
              type="submit"
              value="Zaloguj" />
          </form>
        </div>
      </div>
    );
  }
}
