# Bug Report

### Describe the bug

When generating sourcemaps with a custom `sourcemapBaseUrl`, the emitted sourcemap file contains incorrect content. Instead of the actual sourcemap JSON data, it appears to contain a data URL representation.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    sourcemap: true,
    sourcemapBaseUrl: 'https://cdn.example.com/'
  }
}
```

After building, the generated `.map` file doesn't contain valid JSON sourcemap data. When trying to use the sourcemap for debugging, tools can't parse it correctly.

### Expected behavior

The emitted sourcemap file should contain the standard JSON sourcemap format, regardless of whether `sourcemapBaseUrl` is specified. The base URL should only affect the sourcemap reference in the generated bundle, not the content of the `.map` file itself.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
