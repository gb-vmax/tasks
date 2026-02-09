# Bug Report

### Describe the bug

I'm encountering an issue with whitespace detection in the MDX parser. When processing nodes, the whitespace function is not correctly identifying text nodes and is giving incorrect results for string values.

### Reproduction

```js
// This should return true for whitespace-only text nodes
const textNode = {
  type: 'text',
  value: '   \n  '
}

// Should return true but doesn't work correctly
whitespace(textNode)

// Also having issues with direct string values
whitespace('   \t\n') // Returns unexpected result
```

The function seems to be checking node types incorrectly and the logic for handling string values appears to be inverted.

### Expected behavior

- Text nodes containing only whitespace characters should be identified correctly
- Direct string values that are whitespace-only should return `true`
- Non-whitespace strings should return `false`

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
