# Bug Report

### Describe the bug

When parsing MDX with JSX attributes, the attribute type is being set incorrectly. Regular JSX attributes are being created with type `"mdxJsxAttributeExpression"` instead of `"mdxJsxAttribute"`, which breaks attribute parsing and causes the wrong AST structure to be generated.

### Reproduction

```jsx
// This MDX content with a simple JSX attribute
<Component foo="bar" />

// Results in an incorrect AST node type
// Expected: { type: "mdxJsxAttribute", name: "foo", value: "bar" }
// Actual: { type: "mdxJsxAttributeExpression", name: "foo", value: "bar" }
```

The issue occurs when processing JSX tag attributes during the markdown-to-AST conversion. The attribute type gets misidentified, leading to downstream parsing errors or unexpected behavior when tools try to process the AST.

### Expected behavior

Regular JSX attributes should be parsed as `mdxJsxAttribute` type nodes, not `mdxJsxAttributeExpression`. Expression attributes (like `{...spread}` or `{expression}`) should be the only ones using the expression type.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
