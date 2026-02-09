# Bug Report

### Describe the bug

After a recent update, HTML serialization is producing incorrect output when processing AST nodes. The generated HTML structure appears to be malformed or missing expected elements in certain cases.

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
}

const html = toHtml(tree)
// Output is not as expected
```

### Expected behavior

The HTML output should correctly serialize the AST tree with proper node handling. Parent-child relationships should be maintained and all node properties should be processed in the correct order.

### Additional context

This seems to affect nodes with specific index positions within their parent containers. The issue might be related to how node context is being passed during the serialization process.

---
Repository: /testbed
