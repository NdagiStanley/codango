var React = require("react");
var Team = React.createClass({
  render() {
    return (
      <div class="page-content">
          <div class="row">
              <div class="col-sm-4">
                  <div class="team-members">
                      <div class="team-avatar">
                          <img src="https://avatars2.githubusercontent.com/u/13224175?v=3&s=460" class="img-responsive"/>
                      </div>
                      <div class="team-desc">
                          <a href="https://github.com/andela-ooshodi"><h4>Olufunmilade Oshodi</h4></a>
                          <span>Developer</span>
                      </div>
                  </div>
              </div>
              <div class="col-sm-4">
                  <div class="team-members">
                      <div class="team-avatar">
                          <img src="https://avatars2.githubusercontent.com/u/13223950?v=3&s=460" class="img-responsive"/>
                      </div>
                      <div class="team-desc">
                          <a href="https://github.com/andela-ijubril"><h4>Issa Jubril</h4></a>
                          <span>Developer</span>
                      </div>
                  </div>
              </div>
              <div class="col-sm-4">
                  <div class="team-members">
                      <div class="team-avatar">
                         <img src="https://avatars2.githubusercontent.com/u/15088852?v=3&s=460" class="img-responsive"/>
                      </div>
                      <div class="team-desc">
                           <a href="https://github.com/andela-ashuaib"><h4>Abiodun Shuaib</h4></a>
                          <span>Developer</span>
                      </div>
                  </div>
              </div>
              <div class="col-sm-4">
                  <div class="team-members">
                      <div class="team-avatar">
                         <img src="https://avatars3.githubusercontent.com/u/13269579?v=3&s=460" class="img-responsive"/>
                      </div>
                      <div class="team-desc">
                           <a href="https://github.com/andela-jngatia"><h4>Joan Ngatia</h4></a>
                          <span>Developer</span>
                      </div>
                  </div>
              </div>
              <div class="col-sm-4">
                  <div class="team-members">
                      <div class="team-avatar">
                         <img src="https://avatars2.githubusercontent.com/u/15629602?v=3&s=460" class="img-responsive"/>
                      </div>
                      <div class="team-desc">
                           <a href="https://github.com/andela-sndagi"><h4>Stan MD</h4></a>
                          <span>Developer</span>
                      </div>
                  </div>
              </div>
          </div>
      </div>
    );
  }
});
module.exports = Team;
