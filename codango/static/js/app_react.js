// Main entry point for react components

import { render } from 'react-dom'
import { Router, Route, Link, browserHistory, IndexRoute} from 'react-router';
import React, {Component} from 'react';
import About from './components/about.jsx';
import Main from './components/main.jsx';
import Team from './components/team.jsx';
import Home from './components/home.jsx';
import Community from './components/community.jsx';
import Contact from './components/contact.jsx';
import {Nav, Navbar, NavbarHeader, NavItem, Button} from 'react-bootstrap';


let routes = (<Router history={browserHistory}>
                <Route path="/" component={Main}>
                    <IndexRoute component={Home} history={browserHistory}/>
                    <Route path="/about" component={About}/>
                    <Route path="/team" component={Team}/>
                    <Route path="/contact" component={Contact}/>
                    <Route path="/home" component={Community}/>
                </Route>
              </Router>)

render(routes, document.getElementById('react'));
