import React, { Component } from 'react'



export default class Filter extends Component {
    handle_change = (event) => {
        this.props.setState({todos_filter: event.target.value});
    };

    render() {
        return (
            <select 
                name="todos_filter" 
                id="filter_select"
                defaultValue={1}
                onChange={this.handle_change}>
                <option value={1}>Wszystkie</option>
                <option value={2}>Zrobione</option>
                <option value={3}>Nie zrobione</option>
            </select>
        )
    }
}
