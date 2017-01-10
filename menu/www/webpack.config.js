var path = require('path');
var srcPath = path.join(__dirname, 'src');
var distPath = path.join(__dirname, 'dist');
var CopyWebpackPlugin = require('copy-webpack-plugin');
var webpack = require('webpack');

var config = {
    entry: path.join(srcPath, 'index.js'),
    output: {
        path: path.join(distPath),
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                presets: ["es2015"]
            },
            {
                test: /\.html$/,
                loader: 'html'
            },
            {
                test: /\.sass/,
                loaders: ["style", "css", "sass"]
            },
            {
                test: /\.(png|woff|woff2|eot|ttf|svg)$/,
                loader: 'url-loader?limit=100000'
            }
        ]
    },
    plugins: [
        new CopyWebpackPlugin([
            {from: path.join(srcPath, 'index.html'), to: distPath},
            {from: path.join(srcPath, 'static'), to: distPath}
        ])
    ],
    devtool: "source-map"
};

module.exports = config;
