# Bug Report

### Describe the bug

I'm experiencing an issue with loading CommonJS config files. When I use a config file that exports a default configuration object, the config isn't being loaded properly. Instead of getting my configuration, I'm getting `false` or an unexpected value.

### Reproduction

Create a `rollup.config.js` file with a default export:

```js
module.exports = {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'cjs'
  }
}
```

When running rollup with this config, the configuration doesn't get picked up correctly. The build either fails or uses default settings instead of my custom config.

### Expected behavior

The config file should be loaded and applied correctly. When exporting a configuration object directly (without using `module.exports.default`), rollup should recognize and use that configuration.

### Additional context

This seems to have broken recently. My config files were working fine before, but now I have to restructure them to use `module.exports.default` explicitly, which shouldn't be necessary for CommonJS modules.

---
Repository: /testbed
