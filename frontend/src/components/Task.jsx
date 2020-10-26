import React, { Component } from 'react'
import DoneButton from './DoneButton';



export default class Task extends Component {
    constructor(props) {
        super(props);
        this.state = {
            full_descrpt_viewed: false
        };
    }

    viewFullDescrpt = () => {
        this.setState({
            full_descrpt_viewed: !this.state.full_descrpt_viewed
        });
    }

    formatDatetime = (iso_str) => {
        const monthNames = [
            "stycznia",
            "lutego",
            "marca",
            "kwietnia",
            "maja",
            "czerwca",
            "lipca",
            "sierpnia",
            "września",
            "października",
            "listopada",
            "grudnia"
        ];
        var datetime = new Date(iso_str);
        return datetime.getHours() + ':' + datetime.getMinutes() + ' - ' + datetime.getDay() +
            ' ' + monthNames[datetime.getMonth()] + ' ' + datetime.getFullYear();
    }

    checkIfAfterDeadline = (iso_str) => {
        var deadline_datetime = new Date(iso_str);
        const now = Date.now();
        if (now > deadline_datetime) {
            return true
        }
        else{ return false }
    }

    render() {
        return (
            <div key={this.props.todo.id}>
                <h4
                    className={
                        this.props.todo.done
                        ?
                        "completed-task"
                        :
                        null
                    }>
                    {this.props.todo.name}
                </h4>
                <p
                    className={
                        this.checkIfAfterDeadline(this.props.todo.deadline) && !this.props.todo.done ?
                        "red-text"
                        :
                        null
                    }>
                    Deadline: {this.formatDatetime(this.props.todo.deadline)}
                </p>
                <p>
                    {
                        (this.props.todo.description.length > 40) ?
                            this.state.full_descrpt_viewed ?
                            this.props.todo.description
                            :
                            this.props.todo.description.slice(0, 40) + "..."
                        :
                        this.props.todo.description
                    }
                </p>
                {
                    (this.props.todo.description.length > 40) ?
                    <p 
                        className="action-link"
                        onClick={this.viewFullDescrpt}>
                        {
                            this.state.full_descrpt_viewed ?
                            "Mniej"
                            :
                            "Więcej"
                        }  
                    </p>
                    :
                    null
                }
                {
                    this.props.todo.done ?
                    <div className="btn inactive-btn">Wykonane</div>
                    :
                    <DoneButton 
                        className="btn"
                        instance_id={this.props.todo.id}
                        fetchToDos={this.props.fetchToDos}/>
                }
            </div>
        )
    }
}
