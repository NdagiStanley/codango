import { render } from 'react-dom'
import React, {Component} from 'react';
import { Link } from 'react-router';
import Grid from 'react-bootstrap/lib/Grid';
import Row from 'react-bootstrap/lib/Row';
import Col from 'react-bootstrap/lib/Col';
import {
    form,
    Form,
    FormGroup,
    FormControl,
    Control,
    ControlLabel,
    Checkbox,
    Button,
    Tab,
    Tabs
} from 'react-bootstrap';

class LoginForm extends Component {
    render() {
        return  (
            <form>
                <FormGroup controlId="formControlsText">
                    <ControlLabel>Username</ControlLabel>
                    <FormControl type="text" placeholder="Username" />
                </FormGroup>
                <FormGroup controlId="formControlsPassword">
                    <ControlLabel>Password</ControlLabel>
                    <FormControl type="password" placeholder="Password" />
                </FormGroup>
                <Checkbox>Remember me </Checkbox>
                <FormGroup>
                    <Button type="submit" className="btn btn-primary">Login</Button>
                </FormGroup>
                <FormGroup>
                    <Button type="submit" className="btn btn-primary" inline disabled>Login with Facebook</Button>
                    {' '}
                    <Button type="submit" className="btn btn-danger" inline disabled>Login with Google</Button>
                </FormGroup>
                <p>Forgot password? <a href="/recovery">Reset</a></p>
            </form>
        )
    }
}

class RegisterForm extends Component {
    render() {
        return  (
            <form>
                <FormGroup controlId="formControlsText">
                    <ControlLabel>Username</ControlLabel>
                    <FormControl type="text" placeholder="Username" />
                </FormGroup>
                <FormGroup controlId="formControlsEmail">
                    <ControlLabel>E-mail</ControlLabel>
                    <FormControl type="email" placeholder="Email" />
                </FormGroup>
                <FormGroup controlId="formControlsPassword">
                    <ControlLabel>Password</ControlLabel>
                    <FormControl type="password" placeholder="Password" />
                </FormGroup>
                <FormGroup controlId="formControlsPassword">
                    <ControlLabel>Verify Password</ControlLabel>
                    <FormControl type="password" placeholder="Password" />
                </FormGroup>
                <FormGroup>
                    <Button type="submit" className="btn btn-primary">Register</Button>
                </FormGroup>

            </form>
        )
    }
}

class FormTabs extends Component {
    render() {
        return (
          <Tabs defaultActiveKey={1} id="authentication-forms">
            <Tab eventKey={1} title="Login">
                <LoginForm />
            </Tab>
            <Tab eventKey={2} title="Register">
                <RegisterForm />
            </Tab>
          </Tabs>
        );
    }
}

export default class Home extends Component {
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
};

module.exports = Home;
