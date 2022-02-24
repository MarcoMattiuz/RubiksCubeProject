const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin')
module.exports = {
    entry: "./src/main.js",
    plugins: [
        new HtmlWebpackPlugin({
            template: "./src/index.html",
            title: "3DTest"
        }),
        // new CopyWebpackPlugin({
        //     patterns: [
        //         { from: 'static' }
        //     ]
        // }),
        new CleanWebpackPlugin()

    ],
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
            {
                test: /\.html$/i,
                loader: "html-loader",
            },
            {
                test: /\.(png|jpg|gif)$/i,
                use: [
                    {
                        loader: 'url-loader',
                        options: {
                            limit: 8192,
                        }
                    },
                ],

                type: 'javascript/auto'
            },
        ]


    }
}