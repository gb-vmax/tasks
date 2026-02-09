# Bug Report

### Describe the bug

I'm experiencing an issue where entry chunks are not getting their names properly reserved in the bundle. It seems like the preliminary file names are being generated for the wrong chunks - specifically for chunks that are NOT user-defined entry points, when it should be the opposite.

### Reproduction

```js
// Create a bundle with explicit entry points
const bundle = await rollup({
  input: {
    main: 'src/main.js',
    secondary: 'src/secondary.js'
  }
});

// Generate the bundle
await bundle.generate({
  format: 'es',
  entryFileNames: '[name].js'
});
```

After this change, the entry chunks (main.js and secondary.js) don't have their names properly reserved, which can lead to naming conflicts or unexpected chunk names in the output.

### Expected behavior

Entry chunks that are user-defined entry points should have their preliminary file names generated to reserve those names in the bundle. Non-entry chunks should not have this behavior.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
