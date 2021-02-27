import React, { Component, Fragment } from 'react';



export default class Delete extends Component {

    handleDelete = (instance_id) => {
        fetch(`http://localhost:8000/todo/todos/${instance_id}/`, {
            method: 'DELETE',
            headers: {
            'Content-Type': 'application/json',
                Authorization: `JWT ${localStorage.getItem('token')}`
            },
        })
        .then(this.handleFetchErrors)
        .then(this.props.handleDeleteView())
        .catch(error => { console.log(error); });

        this.props.handleDeleteView();
    }

    handleGoBack = () => {
        this.props.setState({ deleting: false });
    }

    render() {
        return (
            <Fragment>
                <div 
                    onClick={this.handleGoBack}
                    className="blurred-bg"></div>
                <div className="overlay-box delete-box with-shadow">
                    <h3>Czy napewno chcesz usunąć to zadanie?</h3>
                    <button
                        className="btn"
                        onClick={() => ( this.handleDelete(this.props.instance_id) )}>Tak</button>
                    <button 
                        className="btn"
                        onClick={this.handleGoBack}>Anuluj</button>
                </div>
            </Fragment>
        )
    }
}
