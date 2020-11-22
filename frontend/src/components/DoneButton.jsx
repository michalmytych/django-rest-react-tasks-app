import React, { Component } from 'react';



export default class DoneButton extends Component {
    handleDone = (id) => {
        fetch(`http://localhost:8000/todo/todos/${id}/`, {
          method: 'PATCH',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `JWT ${localStorage.getItem('token')}`
          },
          body: JSON.stringify({
              "done": true
          })
        })
        .then(this.props.handleFetchErrors)
        .then(this.props.fetchToDos)
        .catch(error => {
            console.log(error);
        });
    }
 
    render() {
        return (
            <div 
                onClick={() => this.handleDone(this.props.instance_id)}>
                Wykonaj
            </div>
        )
    }
}
