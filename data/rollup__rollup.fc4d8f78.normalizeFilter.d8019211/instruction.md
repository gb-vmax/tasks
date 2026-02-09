# Bug Report

### Describe the bug

I'm experiencing an issue with plugin filtering where the `include` and `exclude` options seem to be inverted. When I specify files to include, they get excluded instead, and vice versa.

### Reproduction

```js
const filter = {
  include: ['src/**/*.js'],
  exclude: ['src/**/*.test.js']
}

// Expected: only non-test JS files in src/ should be included
// Actual: test files are included, regular files are excluded
```

When I pass a filter object with `include` and `exclude` properties, the behavior is backwards - files I want to include are being excluded, and files I want to exclude are being included.

### Expected behavior

The filter should respect the `include` and `exclude` options as specified:
- Files matching `include` patterns should be included
- Files matching `exclude` patterns should be excluded

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
