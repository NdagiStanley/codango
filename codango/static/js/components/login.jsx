import React, { Component } from 'react';
import {
    Button,
    Checkbox,
    ControlLabel,
    form,
    FormGroup,
    FormControl,
} from 'react-bootstrap';
import request from 'superagent';
import { Redirect } from 'react-router';

class LoginForm extends Component {
    constructor() {
        super();
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleFieldChange = this.handleFieldChange.bind(this);
        this.state = {
            username: '',
            password: '',
            token: ''
        }
    }

    handleSubmit(event) {
        event.preventDefault();
        this.loginUser(this.state.username, this.state.password);
    }
    handleFieldChange(event) {
        event.preventDefault();
        let key = event.target.name;
        let value = event.target.value;
        this.setState({
            [key]: value
        });
    }
    loginUser(username, password) {
        request
            .post('/api/v1/auth/login/')
            .send({'username': username, 'password': password })
            .end((err, result) => {
                if (result.body.token) {
                    <Redirect from="/" to="/home"/>
                }
                this.setState({
                    token: result.body.token
                });
                console.log(`response code is ${result.status}`);
                console.log(this.state);
            })
    }
    render() {
        return  (
            <form onSubmit={this.handleSubmit}>
                <FormGroup controlId="formControlsText">
                    <ControlLabel>Username</ControlLabel>
                    <FormControl type="text" placeholder="Username" name="username" onChange={this.handleFieldChange}/>
                </FormGroup>
                <FormGroup controlId="formControlsPassword" >
                    <ControlLabel>Password</ControlLabel>
                    <FormControl type="password" placeholder="Password" name="password" onChange={this.handleFieldChange}/>
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

module.exports = LoginForm
