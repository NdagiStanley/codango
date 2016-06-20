var React = require("react");
var Team = React.createClass({
  render() {
    return (
        <div>
            <div className="heading">
                <h1 className="page-title">Our Awesome Team</h1>
            </div>
            <div className="page-content">
                <div className="row">
                    <div className="col-sm-4">
                        <div className="team-members">
                            <div className="team-avatar">
                                <img src="https://avatars2.githubusercontent.com/u/13224175?v=3&s=460" className="img-responsive"/>
                            </div>
                            <div className="team-desc">
                                <a href="https://github.com/andela-ooshodi"><h4>Olufunmilade Oshodi</h4></a>
                                <span>Developer</span>
                            </div>
                        </div>
                    </div>
                    <div className="col-sm-4">
                        <div className="team-members">
                            <div className="team-avatar">
                                <img src="https://avatars2.githubusercontent.com/u/13223950?v=3&s=460" className="img-responsive"/>
                            </div>
                            <div className="team-desc">
                                <a href="https://github.com/andela-ijubril"><h4>Issa Jubril</h4></a>
                                <span>Developer</span>
                            </div>
                        </div>
                    </div>
                    <div className="col-sm-4">
                        <div className="team-members">
                            <div className="team-avatar">
                               <img src="https://avatars2.githubusercontent.com/u/15088852?v=3&s=460" className="img-responsive"/>
                            </div>
                            <div className="team-desc">
                                 <a href="https://github.com/andela-ashuaib"><h4>Abiodun Shuaib</h4></a>
                                <span>Developer</span>
                            </div>
                        </div>
                    </div>
                    <div className="col-sm-4">
                        <div className="team-members">
                            <div className="team-avatar">
                               <img src="https://avatars3.githubusercontent.com/u/13269579?v=3&s=460" className="img-responsive"/>
                            </div>
                            <div className="team-desc">
                                 <a href="https://github.com/andela-jngatia"><h4>Joan Ngatia</h4></a>
                                <span>Developer</span>
                            </div>
                        </div>
                    </div>
                    <div className="col-sm-4">
                        <div className="team-members">
                            <div className="team-avatar">
                               <img src="https://avatars2.githubusercontent.com/u/15629602?v=3&s=460" className="img-responsive"/>
                            </div>
                            <div className="team-desc">
                                 <a href="https://github.com/NdagiStanley"><h4>Stan MD</h4></a>
                                <span>Developer</span>
                            </div>
                        </div>
                    </div>
                    <div className="col-sm-4">
                        <div className="team-members">
                            <div className="team-avatar">
                               <img src="https://avatars2.githubusercontent.com/u/17288133?v=3&s=460" className="img-responsive"/>
                            </div>
                            <div className="team-desc">
                                 <a href="https://github.com/andela-akiura"><h4>Alex Kiura</h4></a>
                                <span>Developer</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    );
  }
});
module.exports = Team;
