var mocha = require('mocha')
var webpack = require('webpack');
module.exports = function (config) {
    config.set({
        browsers: ['PhantomJS'],
        singleRun: true,
        frameworks: ['mocha'],
        files: [
            'tests.webpack.js'
        ],
        preprocessors: {
            'tests.webpack.js': ['webpack']
        },
        reporters: ['progress'],
        webpack: {
            module: {
                loaders: [
                    {
                        test: /\.jsx?$/,
                        exclude: /node_modules/,
                        loader: 'babel-loader',
                        query: {
                            presets:['react', 'es2015', 'stage-0']
                        }
                    },
                ]
            },
            resolve: {
                alias: {
                    'sinon': 'sinon/pkg/sinon'
                }
            },
            externals: {
                'jsdom': 'window',
                'cheerio': 'window',
                'react/lib/ExecutionEnvironment': true
            },
            watch: true
        },
        webpackServer: {
            noInfo: true
        }
    });
};
