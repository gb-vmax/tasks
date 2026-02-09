# Bug Report

### Describe the bug

I'm encountering an issue with MDX compilation where the opener function seems to be calling callbacks in the wrong order. When processing tokens with an `and` callback, the logic appears inverted - it's only calling the callback when `and` is falsy instead of when it's truthy.

### Reproduction

```js
// When compiling MDX content with nested structures
const mdxContent = `
# Heading

Some content with **bold** and *italic* text.
`;

// The compiler processes tokens but the opener function
// behaves unexpectedly with the 'and' parameter
```

### Expected behavior

The opener function should:
1. Call the `and` callback when it's provided (truthy)
2. Skip calling it when it's not provided (falsy)

Currently it seems to do the opposite - calling `and` only when it doesn't exist, which would cause a runtime error.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This looks like it might be a logic error in the conditional check. The callback should be invoked when `and` exists, not when it doesn't.

---
Repository: /testbed
