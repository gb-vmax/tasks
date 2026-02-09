# Bug Report

### Describe the bug

I'm encountering an issue with MDX compilation where non-JSX content (like plain text or markdown elements) is being incorrectly wrapped in JSX fragments. This causes the output to contain unexpected JSX fragment wrappers around content that should be rendered directly.

### Reproduction

When compiling MDX content that contains elements other than JSX fragments or JSX elements (for example, plain markdown or text nodes), the output incorrectly wraps them in JSX fragments.

```js
// Example MDX content
const mdxContent = `
# Hello World
This is plain text
`;

// After compilation, the output unexpectedly wraps everything in a JSXFragment
// even though the source doesn't contain JSX
```

### Expected behavior

Only content that is already a JSXFragment or JSXElement should remain as-is. Other content types (plain text, markdown elements, etc.) should be wrapped in a JSXFragment for proper rendering. The current behavior seems inverted - it's wrapping things that are already JSX and not wrapping things that aren't.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This might be related to recent changes in the toEstree conversion logic. The wrapping condition seems backwards from what it should be.

---
Repository: /testbed
