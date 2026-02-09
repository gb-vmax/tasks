# Bug Report

### Describe the bug

I'm experiencing an issue with markdown text node serialization. When processing markdown AST nodes that have empty or undefined text values, the output is not being generated correctly. The serialized markdown appears to be missing text content in certain cases.

### Reproduction

```js
const mdast = {
  type: 'text',
  value: 'some content'
}

// Processing this node works fine
const result1 = serialize(mdast)

// But when the value is empty or falsy, output is incorrect
const mdast2 = {
  type: 'text',
  value: ''
}

const result2 = serialize(mdast2)
// Expected: empty string
// Actual: undefined or incorrect output
```

### Expected behavior

Text nodes with empty or falsy values should still be serialized correctly and return the appropriate output. The serializer should handle edge cases like empty strings gracefully.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
