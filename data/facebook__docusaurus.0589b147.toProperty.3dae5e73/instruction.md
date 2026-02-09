# Bug Report

### Describe the bug

I'm experiencing an issue with JSX attribute handling in MDX. When trying to use JSX expression containers in attributes, I'm getting unexpected errors about `JSXEmptyExpression` not being allowed in props, even when the expression is not empty.

Additionally, the generated property objects seem to have the wrong `kind` value - they're being set as getters instead of regular initialized properties.

### Reproduction

```jsx
// Example MDX content
<Component attribute={someValue} />
```

When this is processed, it fails with an error message about `JSXEmptyExpression` not being allowed, even though `someValue` is a valid expression.

Also, when inspecting the generated AST, properties that should be regular key-value pairs (kind: "init") are being marked as getters (kind: "get"), which breaks the expected object structure.

### Expected behavior

1. Valid JSX expressions in attributes should be processed without errors
2. Property objects should have `kind: "init"` for standard attribute assignments, not `kind: "get"`

### System Info
- @mdx-js/mdx version: 3.0.0

This seems like it might be a regression - the logic for validating expression types and setting property kinds appears to be inverted.

---
Repository: /testbed
