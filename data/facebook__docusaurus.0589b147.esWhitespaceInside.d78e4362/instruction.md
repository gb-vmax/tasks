# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where whitespace handling in JSX tags seems to be broken. When there's whitespace (particularly line endings) inside JSX expressions, the parser appears to be getting into an incorrect state.

### Reproduction

```mdx
<Component
  prop={
    value
  }
/>
```

When parsing MDX content with JSX tags that have whitespace or line breaks inside attribute values or expressions, the parser doesn't handle them correctly. The whitespace tokens aren't being properly exited before transitioning states.

### Expected behavior

The parser should correctly handle whitespace and line endings inside JSX expressions and attributes, properly managing state transitions and token exits.

### Additional context

This seems related to the whitespace handling logic in the JSX parser. The issue manifests when there are newlines or other whitespace characters within JSX expressions.

---
Repository: /testbed
