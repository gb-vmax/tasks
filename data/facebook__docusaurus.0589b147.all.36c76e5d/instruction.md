# Bug Report

### Describe the bug

I'm experiencing an issue with HTML rendering where the first child element in a parent node is being skipped during serialization. When converting AST nodes to HTML strings, the output is missing the initial child element.

### Reproduction

```js
const parent = {
  children: [
    { type: 'text', value: 'First' },
    { type: 'text', value: 'Second' },
    { type: 'text', value: 'Third' }
  ]
}

// Expected output: "FirstSecondThird"
// Actual output: "SecondThird"
```

The first child node is consistently being omitted from the rendered output. This affects any parent element with multiple children - the first one just doesn't appear in the final HTML string.

### Expected behavior

All child elements should be included in the serialized HTML output, including the first child. The rendering should process every element in the children array without skipping any.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
