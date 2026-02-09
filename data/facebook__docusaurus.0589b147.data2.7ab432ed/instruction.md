# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX parsing where the order of operations in the `data2` function appears to be incorrect. When processing MDX JSX tokens, the enter and exit callbacks are being called in the wrong sequence, which is causing unexpected behavior during markdown-to-AST transformation.

### Reproduction

```js
// When parsing MDX content with JSX tags
const mdxContent = `
<Component>
  Some content here
</Component>
`

// The data2 function is called during token processing
// but the enter/exit sequence is reversed
```

The issue occurs when the parser processes data tokens within MDX JSX tags. The exit callback is being invoked before the enter callback, and the context (`this`) is not being properly passed to the enter callback.

### Expected behavior

The `data2` function should:
1. Call `this.config.enter.data` first with the correct context
2. Then call `this.config.exit.data` with the correct context
3. Both should receive `this` as the context and `token` as the parameter

### Additional context

This is affecting the remark-mdx parser (version 3.0.0) and may cause issues with proper AST node creation when parsing MDX documents that contain JSX elements with nested content.

---
Repository: /testbed
