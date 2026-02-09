# Bug Report

### Describe the bug

When loading config files, imports with `.json` extensions are not being handled correctly. JSON files are being treated as external dependencies instead of being resolved and included in the bundle.

### Reproduction

Create a rollup config file that imports a JSON file:

```js
// rollup.config.js
import packageJson from './package.json';

export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'cjs'
  },
  // Use package.json data in config
  banner: `/* ${packageJson.name} v${packageJson.version} */`
}
```

When running rollup with this config, the JSON import fails to resolve properly and the config file cannot be loaded.

### Expected behavior

JSON files should be resolved and bundled correctly when imported in the config file. The `.json` extension should be recognized and the file should be treated as a local import, not an external dependency.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
