let React = require("react");
let Formsy = require("formsy-react");
let ReactDOM = require('react-dom');
import {
    Col,
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

let Contact = React.createClass({
    handleFieldChange(event) {
        event.preventDefault()
    },

  render() {
        return (
            <div>
              <div className="row">
                <div className="col-sm-12 col-lg-12">
                    <h1 className="page-title">Contact us <small><em>We'd love to hear from you</em></small></h1>
                </div>
              </div>
              <div className="row">
                  <div className="col-md-8">
                    <div  className="well  well-sm">
                      <Form horizontal action="post" onSubmit={this.props.onClick} className="Contact">
                          <FormGroup controlId="formControlsText">
                              <Col componentClass={ControlLabel} sm={2}>Name</Col>
                               <Col sm={10}>
                                   <FormControl type="text" placeholder="Name" name="name" onChange={this.handleFieldChange}/>
                               </Col>
                          </FormGroup>
                          <FormGroup controlId="formControlsText">
                              <Col componentClass={ControlLabel} sm={2}>Email</Col>
                              <Col sm={10}>
                                  <FormControl type="email" placeholder="Email" name="email" onChange={this.handleFieldChange}/>
                              </Col>
                          </FormGroup>
                          <FormGroup controlId="formControlsText">
                              <Col componentClass={ControlLabel} sm={2}>Subject</Col>
                              <Col sm={10}>
                                  <FormControl type="text" placeholder="Subject" name="subject" onChange={this.handleFieldChange}/>
                              </Col>
                          </FormGroup>
                          <FormGroup controlId="formControlsText">
                              <Col componentClass={ControlLabel} sm={2}>Message</Col>
                              <Col sm={10}>
                                  <FormControl componentClass="textarea" placeholder="Message" name="message" onChange={this.handleFieldChange}/>
                              </Col>
                          </FormGroup>
                          <FormGroup controlId="formControlsText">
                              <Col sm={2}>
                                  <Button type="submit" id="contact" type="submit" className="pull-right btn btn-primary">Send Message</Button>
                              </Col>
                          </FormGroup>
                    </Form>
                    </div>
                  </div>
                  <div className="col-md-4">
                      <address>
                        <strong>Codango, Inc.</strong><br />
                        55 Moleye Street<br />
                        Sabo, Yaba<br />
                        Nigeria<br />
                        0800-codango
                      </address>
                  </div>
                </div>
            </div>
        );
    }
});
module.exports = Contact;
