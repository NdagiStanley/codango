// Main entry point for react components
var React = require('react');
var ReactDOM = require('react-dom');
var About = require('./components/about.jsx');
ReactDOM.render(
    <About />,
    document.getElementById('about-us')
);
