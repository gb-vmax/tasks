# Bug Report

### Describe the bug

The MDX parser is rejecting valid node objects. When processing MDX content with certain node structures, the parser incorrectly identifies valid nodes as invalid, causing parsing to fail or behave unexpectedly.

### Reproduction

```js
const node = {
  type: 'element',
  tagName: 'div',
  children: []
}

// This valid node is being rejected by the parser
// Expected: node should be recognized as valid
// Actual: node is treated as invalid
```

When passing properly structured node objects to the MDX parser, they are not being recognized even though they have all the required properties (`type` as a non-empty string).

### Expected behavior

Valid node objects with a `type` property should be correctly identified and processed by the parser. Any object with `typeof value === "object"` and a valid `type` string property should pass validation.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
