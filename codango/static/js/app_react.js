// Main entry point for react components

import { render } from 'react-dom'
import { Router, Route, Link, browserHistory} from 'react-router';
import React, {Component} from 'react';
import About from './components/about.jsx';
import Team from './components/team.jsx';
import {Nav, Navbar, NavbarHeader, NavItem, Button} from 'react-bootstrap';
// import Contact from './components/contact.jsx';

export default class App extends Component {
    render() {
        return (
            <div>
                <Nav className="navbar navbar-default navbar-fixed-top">
                    <div class="container">
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
                            </ul>
                        </div>
                    </div>
                </Nav>
                {this.props.children}
            </div>


        )
    }
}

let routes = (<Router history={browserHistory}>
                <Route path="/" component={App}>
                  <Route path="/about" component={About}/>
                  <Route path="/team" component={Team}/>
                </Route>
              </Router>)
render(routes, document.getElementById('react'));
