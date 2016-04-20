// import FlipCard from 'react-flipcard';
var React = require("react");
var FlipCard = require("react-flipcard");
var Share = require("react-material-icons/icons/social/share");
var Community = require("react-material-icons/icons/social/people");
var Pair = require("react-material-icons/icons/action/code");
var About = React.createClass({
  getInitialState() {
    return {
      isFlipped: false
    };
  },
  showBack() {
    this.setState({
      isFlipped: true
    });
  },
  showFront() {
    this.setState({
      isFlipped: false
    });
  },
  handleOnFlip(flipped) {
    if (flipped) {
      // this.refs.backButton.getDOMNode().focus();
      this.refs.backButton.focus();
    }
  },
  handleKeyDown(e) {
    if (this.state.isFlipped && e.keyCode === 27) {
      this.showFront();
    }
  },
  render() {
    return (
      <div id="cards">
        {/* Default behavior is horizontal flip on hover, or focus */}
        <FlipCard>
          {/* The first child is used as the front of the card */}
          <div>
            <h4 class="about-h4"><strong>Community</strong></h4>
            <div class="section-icon"><Community /></div>
          </div>
          {/* The second child is used as the back of the card */}
          <div>
            <p>Codango is an ever expanding community of vibrant developers from different stacks and levels, helping each other grow to be even stronger developers</p>
          </div>
        </FlipCard>
        {/* Default behavior is horizontal flip on hover, or focus */}
        <FlipCard>
          {/* The first child is used as the front of the card */}
          <div>
            <h4 class="about-h4"><strong>Sharing Resources</strong></h4>
            <div class="section-icon"><Share /></div>
          </div>
          {/* The second child is used as the back of the card */}
          <div>
            <p>Codango provides a platform for developers from various stacks to upload PDFs, DOCS, code snippets and knowledgable updates making them available for all to learn and use. With endless resources available from the whole world, learning has never been easier.</p>
          </div>
        </FlipCard>
        {/*
          The `disabled` attribute allows turning off the auto-flip
          on hover, or focus. This allows manual control over flipping.
​
          The `flipped` attribute indicates whether to show the front,
          or the back, with `true` meaning show the back.
        */}
        {/* Default behavior is horizontal flip on hover, or focus */}
        <FlipCard>
          {/* The first child is used as the front of the card */}
          <div>
            <h4 class="about-h4"><strong>Pair Programming</strong></h4>
            <div class="section-icon"><Pair /></div>
          </div>
          {/* The second child is used as the back of the card */}
          <div>
            <p>Codango provides a platform where developers can act as mentors to other developers in real time and help grow a community of stronger developers.</p>
          </div>
        </FlipCard>
      </div>
    );
  }
});
module.exports = About;
