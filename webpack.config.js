module.exports = {
    resolve: {
        fallback: {
            "fs": require.resolve("fs-webpack-mock"),
            "path": require.resolve("path-browserify"),
            "os": require.resolve("os-browserify/browser")
        }
    }
};