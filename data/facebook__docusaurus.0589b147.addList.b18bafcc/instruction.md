# Bug Report

### Describe the bug

When passing an array of plugins to the processor, I'm getting an `undefined` error. It seems like the plugin processing is trying to access an element beyond the array bounds.

### Reproduction

```js
const processor = unified()
  .use([
    remarkParse,
    remarkRehype,
    rehypeStringify
  ])

// This throws an error when processing
processor.process('# Hello')
```

The issue occurs when you pass plugins as an array. The processor tries to access an index that doesn't exist in the array, resulting in `undefined` being passed to the `add()` function.

### Expected behavior

The processor should correctly iterate through all plugins in the array and apply them without accessing undefined elements.

### Additional context

This appears to be an off-by-one error in the array iteration logic. The loop condition is checking `<= plugins.length` instead of `< plugins.length`, which causes it to access `plugins[plugins.length]` (which is always undefined for a valid array).

---
Repository: /testbed
