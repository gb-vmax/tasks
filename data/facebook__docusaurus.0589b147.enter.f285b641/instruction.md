# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where nested elements are being added to the wrong parent node in the AST. It seems like the parent-child relationships in the tree structure are getting messed up during compilation.

### Reproduction

```mdx
<div>
  <p>First level</p>
  <div>
    <p>Second level</p>
  </div>
</div>
```

When parsing this MDX content, the nested `<p>Second level</p>` element appears to be attached to the wrong parent in the resulting AST. The tree structure doesn't match the expected nesting hierarchy.

### Expected behavior

The AST should correctly represent the nesting structure with each element being a child of its immediate parent. The second `<p>` tag should be a child of the inner `<div>`, which itself should be a child of the outer `<div>`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
