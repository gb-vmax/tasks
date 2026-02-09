# Bug Report

### Describe the bug

I'm experiencing an issue with syntax extension registration where hooks are not being properly initialized or merged. When trying to use custom syntax extensions, the behavior seems inconsistent - sometimes extensions work, other times they don't get registered at all.

### Reproduction

```js
const all = {};
const extension = {
  text: {
    42: { /* some construct */ }
  }
};

// Try to register the extension
syntaxExtension(all, extension);

// The hook doesn't seem to be set up correctly
// Expected: all.text[42] should contain the construct
// Actual: Behavior is unpredictable
```

### Expected behavior

When registering syntax extensions, the hooks should be properly initialized and constructs should be merged correctly into the target object. Each code point should have its array of constructs set up as expected.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. The extension registration logic appears to be confused about when to initialize new entries vs. when to skip existing ones.

---
Repository: /testbed
