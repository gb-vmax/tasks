# Bug Report

### Describe the bug

I'm experiencing an issue with the HTML serialization where the output is completely wrong when converting a document tree to HTML. Instead of getting the expected HTML string, I'm getting back the original node object.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'element',
      tagName: 'p',
      children: [{type: 'text', value: 'Hello world'}]
    }
  ]
};

const result = toHtml(tree);
// Expected: '<p>Hello world</p>'
// Actual: returns the tree object itself instead of HTML string
```

### Expected behavior

The function should return a serialized HTML string representation of the tree, not the tree object itself.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
