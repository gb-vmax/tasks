# Bug Report

### Describe the bug

I'm encountering an error when trying to use JSX attributes with regular names. The parser is throwing an error saying "Member expressions in attribute names are supported" even though I'm using a simple attribute name, not a member expression.

### Reproduction

```jsx
// This throws an error unexpectedly
<Component userName="test" />

// Even simple attributes fail
<div className="container" />
```

The error message says "Member expressions in attribute names are supported" which doesn't make sense for regular attribute names.

### Expected behavior

Regular JSX attribute names (like `className`, `userName`, etc.) should work without throwing errors. Only actual member expressions in attribute names should be rejected if they're not supported.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
