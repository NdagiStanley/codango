// var webpack = require('webpack');
// module.exports = {
//     entry: [
//       "./codango/static/js/app_react.js"
//     ],
//     output: {
//         path: __dirname + 'codango/static/js/build',
//         filename: "bundle.js"
//     },
//     module: {
//         loaders: [
//             { test: /\.js?$/, loaders: ['babel'], exclude: /node_modules/ },
//             { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader'},
//             { test: /\.css$/, loader: "style!css" }
//         ]
//     },
//     plugins: [
//       new webpack.NoErrorsPlugin()
//     ]
//
// };
var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
module.exports = {
    context: __dirname,
    entry: [
      "./codango/static/js/app_react.js"
    ],
    output: {
      path: __dirname + '/codango/static/js/build',
      filename: "bundle.js"
    },
    module: {
        loaders: [
            { test: /\.jsx?$/, loaders: ['react-hot', 'babel-loader'], exclude: /node_modules/ }, // to transform JSX into JS
        ]
    },
    plugins: [
      new BundleTracker({filename: './webpack-stats.json'}),
    ],
    resolve: {
        modulesDirectories: ['node_modules', 'bower_components'],
        extensions: ['', '.js', '.jsx']
    },
};
