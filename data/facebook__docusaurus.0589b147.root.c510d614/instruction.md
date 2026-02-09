# Bug Report

### Describe the bug

After a recent update, the root node transformation appears to be broken. The children of the root node are not being properly included in the output when converting mdast to hast.

### Reproduction

```js
const mdast = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [
        { type: 'text', value: 'Hello world' }
      ]
    }
  ]
}

// Convert mdast to hast
const hast = toHast(mdast)

// Expected: hast.children should contain the transformed paragraph
// Actual: hast.children is empty
console.log(hast.children) // []
```

### Expected behavior

The root node should contain all transformed children from the mdast tree. The `state.all(node)` result should be wrapped and assigned to the children property of the output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
