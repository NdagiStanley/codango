var React = require("react");
import { shallow } from 'enzyme';
// About-us-test.jsx
var About = require('../components/about.jsx');

describe('<About/>', function () {
    it("it the about-us page elements", function () {
        const wrapper = shallow(<About/>);
        expect(wrapper.find('#cards')).to.have.length(3);
    });
});

describe('Sample Test', function() {
    it("should return true for obvious assertion", function() {
        expect(1).toEqual(1);
    });
});
