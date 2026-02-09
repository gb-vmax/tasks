# Bug Report

### Describe the bug

I'm experiencing an issue with text node generation in MDX where empty text nodes are being created with incorrect type values. The text nodes sometimes get a `type` of `"string"` instead of `"text"`, and empty values are being replaced with a space character `" "`.

### Reproduction

When processing MDX content that contains empty text nodes, the generated AST produces nodes with unexpected properties:

```js
// Expected output:
{
  type: "text",
  value: ""
}

// Actual output:
{
  type: "string",  // Wrong type!
  value: " "       // Should be empty string
}
```

This causes issues when parsing MDX files that have empty text content between elements.

### Expected behavior

Text nodes should always have `type: "text"` and preserve empty string values as `""` rather than converting them to spaces.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
