# Bug Report

### Describe the bug

When parsing MDX with attribute values that contain quoted strings, the token ordering appears to be incorrect. The literal marker token is being entered before the literal type token, which seems backwards from the expected structure.

### Reproduction

```mdx
<Component prop="value" />
```

When parsing this MDX, the token tree structure for the attribute value doesn't match what's expected. The marker (quote character) token is being created before its parent literal token, leading to an inverted tree structure.

### Expected behavior

The attribute value literal type should be entered before the marker type, so that the marker is properly nested within the literal token. This is consistent with how other parts of the MDX parser structure their token trees.

### Additional context

This affects any MDX component with quoted attribute values (using either `"` or `'`). The parser still works but the token tree structure is malformed, which could cause issues for tools that analyze or transform the AST.

---
Repository: /testbed
