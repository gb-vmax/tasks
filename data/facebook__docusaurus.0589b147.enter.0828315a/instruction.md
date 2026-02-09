# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where nested elements seem to be getting attached to the wrong parent in the AST. The structure of the parsed output is incorrect - child nodes are appearing under their grandparent instead of their direct parent.

### Reproduction

```js
const mdx = `
<Parent>
  <Child>
    <GrandChild />
  </Child>
</Parent>
`

// After parsing, GrandChild appears as a sibling to Child
// instead of being nested inside Child
```

When I parse this MDX content, the resulting tree structure doesn't match the expected nesting. It looks like child elements are being pushed one level too high in the hierarchy.

### Expected behavior

The AST should maintain the proper parent-child relationships. Each node should be added as a child of its immediate parent, not its grandparent.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
