import React from 'react';
const expect = require('expect');
import { shallow , mount, render } from 'enzyme';
// Team page-test.jsx
import Team from '../components/team.jsx';

describe('<Team/>', () => {
    it("it tests the team page elements", () => {
        const wrapper = shallow(<Team/>);
        expect(wrapper.find('.team-members').length).toBe(6);
    });
});
