# Bug Report

### Describe the bug

I'm experiencing an issue with chunk graph generation where all chunks seem to be getting the same rendered chunk info instead of their individual info. When building a project with multiple entry points, the output appears to reference the wrong chunk metadata.

### Reproduction

```js
// rollup.config.js
export default {
  input: {
    main: 'src/main.js',
    secondary: 'src/secondary.js',
    vendor: 'src/vendor.js'
  },
  output: {
    dir: 'dist',
    format: 'es'
  }
}
```

When I build this configuration, all chunks in the generated graph have identical `fileName` and metadata properties, even though they should each have their own unique information. It looks like the first chunk's info is being reused for all entries instead of each chunk getting its own rendered info.

### Expected behavior

Each chunk in the graph should have its own unique `fileName` and rendered chunk information based on that specific chunk's properties, not all pointing to the same chunk's data.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
