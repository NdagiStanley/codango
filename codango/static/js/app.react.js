// Main entry point for react components

import { render } from 'react-dom';
import { Router, Route } from 'react-router';
import React from 'react';
import Main from './components/main.jsx';
import Team from './components/team.jsx';

let routes = (<Router>
                <Route path="/" component={Main}>
                    <Route path="/team" component={Team}/>
                </Route>
              </Router>)

render(routes, document.getElementById('react'));
