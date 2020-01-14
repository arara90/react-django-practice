// load babel load
module.exports = {
    module:{
        rules: [
            {
                test:/\.js$/, //any js files
                exclude: /node_modules/,
                use:{
                    loader: "babel-loader"
                }
            }
        ]
    }
}