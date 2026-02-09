# Bug Report

### Describe the bug

I'm encountering an issue with parsing MDX content where the parser seems to be accessing the wrong context. When processing certain MDX structures, I'm getting `undefined` values where I should be getting valid context objects, which is causing parsing to fail or produce incorrect output.

### Reproduction

```js
// When parsing MDX with nested braces or complex structures
const mdxContent = `
# Test

{someExpression}

More content here
`;

// The parser fails to correctly identify the context
// and returns undefined instead of the expected context object
```

### Expected behavior

The parser should correctly track and return the current parsing context at all times. When `curContext()` is called, it should always return a valid context object from the context stack, not `undefined`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to be related to how the context array is being accessed. The current context should always be retrievable from the context stack.

---
Repository: /testbed
