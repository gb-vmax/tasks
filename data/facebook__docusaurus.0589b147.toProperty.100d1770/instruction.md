# Bug Report

### Describe the bug

I'm encountering an issue with JSX attribute handling in MDX. When I use JSX attributes with expression values or boolean shorthand, the generated output is incorrect.

### Reproduction

```jsx
// Case 1: Attribute with JSX expression
<Component disabled={someExpression} />

// Case 2: Boolean shorthand attribute
<Component disabled />
```

For Case 1, it seems like the attribute value is being replaced with something unexpected instead of using the actual expression.

For Case 2, when using boolean shorthand (just `disabled` without a value), the attribute is being set to `false` instead of `true`, which breaks the expected JSX behavior.

### Expected behavior

- Attributes with JSX expressions should preserve the expression value
- Boolean shorthand attributes (like `disabled`, `checked`, etc.) should default to `true` when no value is provided, following standard JSX conventions

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is breaking existing MDX files that rely on standard JSX attribute behavior. Any help would be appreciated!

---
Repository: /testbed
