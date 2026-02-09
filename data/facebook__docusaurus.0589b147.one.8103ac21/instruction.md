# Bug Report

### Describe the bug

I'm experiencing an issue with HTML serialization where the output is incomplete or missing content. When converting AST nodes to HTML strings, some elements are not appearing in the final output even though they exist in the tree structure.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
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
  ]
};

const html = toHtml(tree);
console.log(html);
// Expected: <div>Hello World</div>
// Actual: Empty or incomplete output
```

### Expected behavior

The `toHtml` function should return a complete HTML string representation of the entire tree structure, including all nested elements and text nodes.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
