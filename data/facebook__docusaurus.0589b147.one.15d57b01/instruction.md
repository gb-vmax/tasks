# Bug Report

### Describe the bug

I'm encountering an issue with HTML serialization where the output is malformed or incorrect when converting AST nodes to HTML strings. The generated HTML doesn't match the expected structure, particularly when dealing with nested elements or elements at specific positions in the tree.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'element',
      tagName: 'div',
      children: [
        {
          type: 'element',
          tagName: 'span',
          children: [{ type: 'text', value: 'Hello' }]
        }
      ]
    }
  ]
}

const html = toHtml(tree)
// Output is incorrect or throws an error
```

### Expected behavior

The HTML should be properly serialized with correct node handling, respecting the parent-child relationships and index positions of elements in the tree structure.

### System Info

- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
