# Bug Report

### Describe the bug

When generating sourcemaps with custom `sourcemapFileName` placeholders, the sourcemap file reference is incorrect. The generated sourcemap filename doesn't match what's actually written to the bundle, causing sourcemap loading to fail.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle-[hash].js',
    sourcemap: true,
    sourcemapFileName: 'maps/[name]-[hash].js.map'
  }
}
```

When building with this config:
1. The sourcemap file is created at `maps/bundle-abc123.js.map`
2. But the bundle references a different path in the sourcemap comment
3. Browser fails to load the sourcemap

### Expected behavior

The sourcemap filename in the bundle's sourcemap comment should match the actual file written to disk. If `sourcemapFileName` is specified, the generated reference should use that exact path.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
