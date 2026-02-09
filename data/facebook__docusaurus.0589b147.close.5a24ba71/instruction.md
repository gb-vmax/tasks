# Bug Report

### Describe the bug

I'm experiencing an issue with the remark compiler where closing tokens are not being processed correctly. It appears that the exit handler logic has been inverted - the callback function is now being called when it shouldn't be, and not called when it should be.

### Reproduction

```js
// When processing markdown with nested structures
const processor = remark()
  .use(somePlugin)
  .process(markdownText)

// The closing of tokens behaves incorrectly
// Expected: and() callback should be called when it exists
// Actual: and() callback is called when it's undefined/null
```

This is causing unexpected behavior when parsing markdown documents with nested elements like lists, blockquotes, or code blocks. The exit handlers are being invoked at the wrong times, leading to malformed AST structures.

### Expected behavior

The `and` callback should be executed when it's provided (truthy), not when it's missing (falsy). The current behavior seems backwards.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
