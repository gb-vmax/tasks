# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace detection in MDX content. Text nodes that should be considered empty/whitespace-only are now being treated as non-empty, which is causing unexpected rendering behavior.

### Reproduction

```js
// This text node should be detected as whitespace-only
const textNode = {
  type: 'text',
  value: '   \n\t  '
}

// whitespace() should return true but returns false
const result = whitespace(textNode)
console.log(result) // Expected: true, Actual: false
```

The same issue occurs with plain string values:

```js
const emptyString = '  \n  '
// empty4() should return true but returns false
const result = empty4(emptyString)
console.log(result) // Expected: true, Actual: false
```

### Expected behavior

Strings and text nodes containing only whitespace characters (spaces, tabs, newlines) should be correctly identified as empty. This is important for proper MDX parsing and rendering.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
