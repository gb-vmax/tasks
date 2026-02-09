# Bug Report

### Describe the bug

I'm experiencing an issue with the output file naming pattern when using the `format` placeholder. It seems like the format value is being modified or mutated in an unexpected way, which is causing issues with my build configuration.

### Reproduction

```js
const outputOptions = {
  file: 'dist/[name]-[format].js',
  format: 'esm'
}

// After building, the format placeholder doesn't resolve correctly
// or the format object gets mutated during the pattern resolution
```

When I use the `[format]` placeholder in my output file pattern, something weird happens with the format value. It looks like the format is getting changed or corrupted during the pattern substitution process.

### Expected behavior

The `[format]` placeholder should consistently return the correct format string ('esm', 'cjs', etc.) without any side effects or mutations to the original format configuration.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
