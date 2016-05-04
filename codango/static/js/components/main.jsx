import { render } from 'react-dom'
import React, {Component} from 'react';
import Menu from './menu.jsx'

export default class Main extends Component {
    constructor() {
        super();
    }

    render() {
        return(
            <div>
                <Menu />
                {this.props.children}
            </div>
        )
    }
}

module.exports = Main;
