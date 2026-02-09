# Bug Report

### Describe the bug

I'm experiencing an issue where the MDX processor crashes with an "undefined is not a function" error when processing plugins. This appears to be happening when iterating through the plugin list.

### Reproduction

```js
const processor = createProcessor({
  plugins: [
    remarkGfm,
    rehypeSlug,
    rehypeAutolinkHeadings
  ]
});

// Process some MDX content
await processor.process('# Hello World');
```

The error occurs during plugin initialization. It seems like the processor is trying to access an element beyond the array bounds, which results in trying to call `add()` with `undefined`.

### Expected behavior

The processor should correctly iterate through all plugins in the array and process them without errors. Each plugin should be added exactly once without accessing undefined elements.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
