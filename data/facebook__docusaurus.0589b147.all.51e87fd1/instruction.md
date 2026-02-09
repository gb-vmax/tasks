# Bug Report

### Describe the bug

I'm experiencing an issue with HTML rendering where the first child element in a node is being skipped/missing from the output. When processing nodes with multiple children, only the second child onwards appear in the final HTML string.

### Reproduction

```js
const node = {
  type: 'element',
  tagName: 'div',
  children: [
    { type: 'text', value: 'First' },
    { type: 'text', value: 'Second' },
    { type: 'text', value: 'Third' }
  ]
}

// Expected output: "FirstSecondThird"
// Actual output: "SecondThird"
```

The first child is consistently missing from the rendered output. This affects any parent node with multiple children - the first one is always dropped.

### Expected behavior

All children should be included in the output string in the correct order. The first child element should not be skipped.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
