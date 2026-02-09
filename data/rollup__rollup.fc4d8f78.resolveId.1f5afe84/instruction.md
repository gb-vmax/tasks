# Bug Report

### Config file loading broken for external dependencies

I'm experiencing an issue where external npm packages imported in my Rollup config file are not being resolved correctly. The build fails when trying to load the config file that imports external dependencies.

### Reproduction

Create a `rollup.config.js` file that imports an external package:

```js
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';

export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'cjs'
  },
  plugins: [resolve(), commonjs()]
};
```

When running rollup with this config, it fails to load the config file because the external imports (`@rollup/plugin-node-resolve` and `@rollup/plugin-commonjs`) are not being treated as external dependencies.

### Expected behavior

External npm packages imported in the config file should be resolved from `node_modules` and the config should load successfully. This was working fine before.

### Additional context

The error occurs during the config file loading phase. It seems like the logic for determining what counts as an "external" import might have changed.

---
Repository: /testbed
