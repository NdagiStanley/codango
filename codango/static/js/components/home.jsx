import { render } from 'react-dom'
import React, {Component} from 'react';
import Grid from 'react-bootstrap/lib/Grid';
import Row from 'react-bootstrap/lib/Row';
import Col from 'react-bootstrap/lib/Col';

export default class Home extends Component {
    render() {
        return (
            <Grid>
                <Row className="show-grid">
                  <Col md={8}>
                    <div className="jumbotron">
                      <h1 id="index-h1">Join Our Community</h1>
                      <h3 className="section-text">Codango is a social networking site that connects all types of developers allowing for sharing resources, joining various communities and pair programming </h3>
                      <p><a className="btn btn-primary btn-lg" role="button"><Link to="/about">About</Link></a></p>
                    </div>
                  </Col>
                  <Col md={4}>
                  </Col>
                </Row>
            </Grid>
        );
    }
};
module.exports = Home;
