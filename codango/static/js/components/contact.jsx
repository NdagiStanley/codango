let React = require("react");
let Formsy = require("formsy-react");
let ReactDOM = require('react-dom');
let Contact = React.createClass({
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
                    <div  className="well">
                      <form action="post" onSubmit={this.props.onClick} className="Contact">
                        <div className="Name">
                            <input type="text" name="Name" onChange={this.props.onChange}/>
                            <label>Name</label>
                        </div>
                        <div className="Email">
                            <input type="email" name="Email" onChange={this.props.onChange}/>
                            <label>Email</label>
                        </div>
                        <div className="Subject">
                            <input type="text" name="Subject" onChange={this.props.onChange}/>
                            <label>Subject</label>
                        </div>
                         <div className="Message">
                            <input type="text" name="Message" onChange={this.props.onChange}/>
                            <label>Message</label>
                        </div>
                        <div>
                          <button id="contact" type="submit" className="mdl-button mdl-js-button" >Send Message</button>
                        </div>
                      </form>
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
