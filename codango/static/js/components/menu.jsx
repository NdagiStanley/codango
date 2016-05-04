import { render } from 'react-dom'
import { Router, Route, Link, browserHistory} from 'react-router';
import React, {Component} from 'react';
import {Nav, Navbar, NavbarHeader, NavItem, Button} from 'react-bootstrap';

export default class Menu extends Component {
    render() {
        return (
            <div>
                <Nav className="navbar navbar-default navbar-fixed-top">
                    <div className="container">
                        <div className="navbar-header">
                            <Button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                                <span className="sr-only">Toggle navigation</span>
                                <span className="icon-bar"></span>
                                <span className="icon-bar"></span>
                                <span className="icon-bar"></span>
                            </Button>
                            <a className="navbar-brand" href="/"><img src="../static/img/codango-logo.png"/></a>
                        </div>
                        <div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                            <ul className="nav navbar-nav navbar-right">
                                <li><Link to="/about">About</Link></li>
                                <li><Link to="/team">Team</Link></li>
                                <li><Link to="/contact">Contact us</Link></li>
                            </ul>
                        </div>
                    </div>
                </Nav>
                {this.props.children}
            </div>
        )
    }
}
module.exports = Menu;
