# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX tokenizer where the `onsuccessfulcheck` callback seems to be causing problems. After a recent change, the restore function is no longer being called properly when it should be.

### Reproduction

When processing MDX content with certain constructs, the tokenizer's check mechanism doesn't restore the parser state correctly. This happens when:

1. A construct check succeeds
2. The `onsuccessfulcheck` callback is invoked
3. The state should be restored but isn't

Example scenario:
```js
// Process MDX content that triggers construct checking
const result = compile('some mdx content with special constructs');
// Parser state is not restored as expected
```

### Expected behavior

The `info.restore()` function should be called when a construct check succeeds, allowing the parser to backtrack and try alternative parsing paths when needed. The current behavior prevents proper state restoration.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
