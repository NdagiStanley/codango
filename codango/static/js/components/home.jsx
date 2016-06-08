import React, { Component } from 'react';
import { Link } from 'react-router';
import {
    Col,
    Grid,
    Row,
    Tab,
    Tabs
} from 'react-bootstrap';
import LoginForm from './login.jsx';
import RegisterForm from './register.jsx';

class FormTabs extends Component {
    render() {
        return (
          <Tabs defaultActiveKey={1} id="authentication-forms">
            <Tab eventKey={1} title="Login">
                <LoginForm url="/api/v1/auth/login/"/>
            </Tab>
            <Tab eventKey={2} title="Register">
                <RegisterForm />
            </Tab>
          </Tabs>
        );
    }
}

class Home extends Component {
    render() {
        return (
            <Grid>
                <Row className="show-grid">
                    <Col md={8}>
                        <div className="jumbotron">
                            <h1 id="index-h1">Join Our Community</h1>
                            <h3 className="section-text">Codango is a social networking site that connects all types of developers allowing for sharing resources, joining various communities and pair programming </h3>
                            <Link className="btn btn-primary btn-lg" to="/about">Learn more</Link>
                        </div>
                    </Col>
                    <Col md={4}>
                        <FormTabs />
                    </Col>
                </Row>
            </Grid>
        );
    }
}

module.exports = Home;
