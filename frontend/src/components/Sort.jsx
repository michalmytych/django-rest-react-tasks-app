import React, { Component } from 'react'



export default class Sort extends Component {
    handle_change = (event) => {
        this.props.setState({todos_sort_order: event.target.value});
    };

    render() {
        return (
            <select 
                name="todos_sort_order" 
                id="order_select"
                defaultValue={2}
                onChange={this.handle_change}>
                <option value={1}>Od najstarszych</option>
                <option value={2}>Od najnowszych</option>
            </select>
        )
    }
}
