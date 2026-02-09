# Bug Report

### Describe the bug

I'm experiencing an issue with HTML generation when processing root nodes. The output appears to be empty or incomplete when converting a tree structure to HTML.

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
          type: 'text',
          value: 'Hello World'
        }
      ]
    }
  ]
}

// When converting to HTML, the children are not being processed
const html = toHtml(tree)
// Expected: '<div>Hello World</div>'
// Actual: '' (empty string or missing content)
```

### Expected behavior

When processing a root node, all child elements should be properly converted to HTML. The root node should iterate through its children and generate the complete HTML output.

### System Info
- rehype-stringify: 10.0.0

---
Repository: /testbed
