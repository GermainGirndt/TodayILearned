# CSS Modules - Webpack

## Requirements (Here)

- Create React App

## Implementing Specific Class Names (and not random ones )

- **Root/config/webpack.config.dev.js** and **Root/config/webpack.config.prod.js**

- Adding modules (CSS Modules)
- Added a specific localIdentName (not required)

```
test: /\.css$/,
use: [
    require.resolve('style-loader'),
    {
        loader: require.resolve('css-loader'),
        options: {
            importLoaders: 1,
            modules: true,
            localIdentName: '[name]__[local]__[hash: base64:5]'
        }
    }
]
```
