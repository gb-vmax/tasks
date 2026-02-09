# Bug Report

### Describe the bug

When using the `intro` option in the output configuration, the intro text is not being added to the bundle output. Instead, it seems like the intro content is being lost and only the banner is affected.

### Reproduction

```js
const bundle = await rollup({
  input: 'src/main.js',
  // ... other options
});

await bundle.write({
  file: 'dist/bundle.js',
  format: 'esm',
  intro: '/* This is intro text */',
  banner: '/* This is banner text */'
});
```

### Expected behavior

The generated bundle should include both the intro text and banner text with proper spacing. The intro should appear after the banner but before the actual code.

Expected output structure:
```
/* This is banner text */

/* This is intro text */

// actual code here
```

### Actual behavior

The intro text is missing from the output, and the banner seems to get extra spacing added instead.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
