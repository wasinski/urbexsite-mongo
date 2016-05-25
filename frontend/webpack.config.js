var webpack = require('webpack');
var path = require("path");


var config = {
    context: __dirname + '/app',
    resolve: {
        root: [
            path.resolve('./app')
        ]
    },
    entry: [
        './index.jsx'
    ],
    devServer: {
        historyApiFallback: true,
        host: "0.0.0.0"
    },
    output: {
        path: __dirname + '/app',
        filename: 'bundle.js',
        publicPath: '/'
    },
    plugins: [
        new webpack.DefinePlugin({
            ON_TEST: process.env.NODE_ENV === 'test'
        })
    ],
    module: {
        loaders: [
            {test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel', query: {presets: ['react', 'es2015', 'stage-1']}},
            {test: /\.html$/, loader: 'raw', exclude: /node_modules/},
            {test: /\.css$/, loader: 'style!css', exclude: /node_modules/},
            {test: /\.scss$/, loader: 'style!css!sass', exclude: /node_modules/},
            {test: /\.(ttf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/, loader: 'file-loader'},
            {test: /\.(ico|txt)$/, loader: 'file-loader'},
            {test: /\.png$/, loader: "url-loader?limit=100000"},
            {test: /\.(jpg|gif)$/, loader: "file-loader"}
        ]
    }
};

if (process.env.NODE_ENV === 'production') {
    config.output.path = __dirname + '/dist';
    config.plugins.push(new webpack.optimize.UglifyJsPlugin());
    config.devtool = 'source-map';
}

module.exports = config;
