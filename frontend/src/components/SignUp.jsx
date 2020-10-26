import React, { Fragment } from 'react';



export default class SignupForm extends React.Component {
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
      <Fragment>
        <div
            onClick={this.handleFormQuit}  
            className="blurred-bg"></div>
        <div className="overlay-box with-shadow">
          <form onSubmit={e => this.props.handle_signup(e, this.state)}>
            <h4>Rejestracja</h4>
            <label htmlFor="username">Nazwa użytkownika:</label>
            <input
              type="text"
              name="username"
              value={this.state.username}
              onChange={this.handle_change}
            />
            <label htmlFor="password">Hasło:</label>
            <input
              type="password"
              name="password"
              value={this.state.password}
              onChange={this.handle_change}
            />
            <input
              className="btn"
              type="submit"
              value="Zarejestruj" />
          </form>
        </div>
      </Fragment>
    );
  }
}
