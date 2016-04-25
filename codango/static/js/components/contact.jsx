var React = require("react");
var Contact = React.createClass({
  render() {
    return (
        <div class="row">
            <div class="col-sm-12">
                {% if messages %}
                    {% for message in messages %}
                    <div class="alert alert-{{ message.tags }}" role="alert" id="flash-message">
                        {{ message }}
                    </div>
                    {% endfor %}
                {% endif %}
            </div>
        </div>
        <div class="page-content">
            <div class="row">
                <div class="col-md-8">
                    <div class="well well-sm">
                        <!-- contact us form -->
                        <form role="form" action="/contact-us" method="post" id="contactus-form">
                            {% csrf_token %}
                            {{ contactusform|bootstrap }}
                            <div class="form-group">
                                <button id="send-mssg-btn" type="submit" class="btn btn-primary">Send Message</button>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="col-md-4">
                    <legend><span class="mdi mdi-earth"></span> Our office</legend>
                    <address>
                        <strong>Codango, Inc.</strong><br>
                        55 Moleye Street<br>
                        Sabo, Yaba<br>
                        Nigeria<br>
                        0800-codango
                    </address>
                </div>
            </div>
        </div>
    }
});
module.exports = Contact;
Add Comment
