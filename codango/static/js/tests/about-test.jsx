import React from 'react';
const expect = require('expect');
let FlipCard = require("react-flipcard");
import { shallow , mount, render } from 'enzyme';
// About-us-test.jsx
import About from '../components/about.jsx';

describe('<About/>', () => {
    it("it tests the about-us page elements", () => {
        const wrapper = shallow(<About/>);
        expect(wrapper.contains(FlipCard)).toBe(true);
        expect(wrapper.find(FlipCard).length).toBe(3);
    });
});
