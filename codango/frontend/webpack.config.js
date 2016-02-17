// require all dependencies
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    // absolute path to resolve the entry option
    context: __dirname,

    // entry point
    entry: './assets/js/index',

    output: {
        // storage for compiled bundle
        path: path.resolve('./blog/static/js'),
        // naming convention for compiled bundle
        filename: "bundle.js",
    },

    plugins: [
        // storage of data on compiled bundles
        new BundleTracker({filename: './webpack-stats.json'}),
        // make jquery available in all modules
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        })
    ],

    module: {
        loaders: [
            // regex to show webpack to use these loaders on all .js and .jsx files
            {test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['react']
                }
            }
        ]
    },

    resolve: {
        // show location of webpack-required modules
        modulesDirectories: ['node_modules'],
        extensions: ['', '.js', '.jsx']
    }
}
