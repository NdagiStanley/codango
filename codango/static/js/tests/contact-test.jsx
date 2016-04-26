import React from 'react';
const expect = require('expect');
import { shallow , mount, render } from 'enzyme';
// Contact page-test.jsx
import Contact from '../components/contact.jsx';

describe('<Contact/>', () => {
    it("it tests the contact page elements", () => {
        const wrapper = shallow(<Contact/>);
        expect(wrapper.find('.row').length).toBe(2);
    });
});
