# Bug Report

### Describe the bug

The `enterContainer` function in the remark-directive markdown handler is broken. When processing container directives, I'm getting a runtime error because the function is trying to call `apply` on a token object instead of properly using the context.

### Reproduction

```js
// When parsing markdown with container directives like:
// :::note
// Some content
// :::

// The enterContainer function is called during tokenization
// This causes an error because token.apply is not a function
```

### Expected behavior

Container directives should be parsed correctly without throwing errors. The `enter` function should be called with the proper context (`this`) and the correct arguments, similar to how `enterLeaf` works.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
