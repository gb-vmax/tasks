# Bug Report

### Describe the bug

I'm experiencing an issue with HTML serialization where the output is completely broken. When converting AST nodes to HTML strings, the generated markup appears corrupted or incorrect.

### Reproduction

```js
const tree = {
  type: 'element',
  tagName: 'div',
  properties: {},
  children: [
    {
      type: 'text',
      value: 'Hello World'
    }
  ]
}

const html = toHtml(tree)
// Expected: <div>Hello World</div>
// Actual: Broken/incorrect output
```

### Expected behavior

The HTML serialization should correctly process the AST and generate valid HTML markup with proper node ordering and context.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
