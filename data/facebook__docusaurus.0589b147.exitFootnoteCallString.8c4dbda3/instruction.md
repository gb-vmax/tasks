# Bug Report

### Describe the bug

I'm experiencing an issue with footnote references in the remark-gfm parser. When processing footnote call strings, the label is not being properly assigned to the footnote reference node. The footnote references appear to be missing their labels in the parsed output.

### Reproduction

```js
const footnoteNode = {
  type: 'footnoteReference',
  identifier: '',
  label: ''
};

// Process a footnote like [^1]
// Expected: node.label should be set to the resolved label value
// Actual: node.label remains empty or undefined
```

When parsing markdown with footnote syntax like `[^1]`, the footnote reference nodes in the AST don't have their `label` property correctly populated. The identifier gets set, but the label stays empty.

### Expected behavior

The footnote reference node should have both the `label` and `identifier` properties correctly assigned after parsing footnote call strings.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
