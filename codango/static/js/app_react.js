// Main entry point for react components
const React = require('react');
const ReactDOM = require('react-dom');
const About = require('./components/about.jsx');

ReactDOM.render(
    <About />,
    document.getElementById('about-us')
);
