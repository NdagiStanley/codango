// tests.webpack.js
var context = require.context('./codango/static/js/tests', true, /-test\.jsx$/);
context.keys().forEach(context);
