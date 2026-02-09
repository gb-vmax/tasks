# Bug Report

### Describe the bug

I'm experiencing an issue with JSX tag parsing where tags followed by non-whitespace characters are being incorrectly accepted. It seems like the parser is allowing invalid syntax that should be rejected.

### Reproduction

```jsx
// This should fail but is being accepted
<div>content</div>x

// Similarly, this invalid syntax passes
<Component/>invalid
```

The parser should reject JSX tags when they're immediately followed by non-whitespace characters without proper separation, but currently these malformed tags are being parsed successfully.

### Expected behavior

JSX tags should only be valid when followed by whitespace or line endings. Tags like `<div/>x` or `<Component>test</Component>abc` should be rejected as invalid syntax since they have non-whitespace characters immediately after the closing tag without proper separation.

### Additional context

This appears to be a regression in the tag parsing logic. The validator seems to be checking for whitespace/line endings but then proceeding incorrectly when non-whitespace is encountered.

---
Repository: /testbed
