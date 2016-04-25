var expect = require('expect');
var React = require("react");
// About-us-test.jsx
// var TestUtils = require('react-addons-{TestUtils}'),
var TestUtils = require('react-addons-test-utils');
var About = require('../components/about.jsx');
describe('about', function () {
    it("renders a flipcard", function () {
        var about = TestUtils.renderIntoDocument(
            <About />
        );
        var flipcard = TestUtils.findRenderedDOMComponentWithTag(
                about, 'flipcard'
        );
        expect(flipcard.getDOMNode().textContent).toEqual("Community");
    });
});
describe('Sample Test', function() {
  it("should return true for obvious assertion", function() {
    expect(1).toEqual(1);
  })
})
