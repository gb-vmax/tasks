# Bug Report

### Describe the bug

I'm encountering an issue with custom data properties when transforming markdown to HTML. When I set `hChildren` in the data object of a markdown node, the resulting HTML element doesn't include those children correctly.

### Reproduction

```js
const mdast = {
  type: 'paragraph',
  children: [{ type: 'text', value: 'original content' }],
  data: {
    hChildren: [{ type: 'text', value: 'custom child' }]
  }
}

// After transformation, the custom children from hChildren are not present
// Only the original children appear in the output
```

### Expected behavior

When `hChildren` is specified in the node's data object, those children should be used in the resulting HTML element. The custom children defined in `hChildren` should replace or be included in the final output.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
