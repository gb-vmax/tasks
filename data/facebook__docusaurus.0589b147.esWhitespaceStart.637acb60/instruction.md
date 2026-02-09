# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where whitespace handling in JSX tags appears to be broken. After a line ending within JSX expressions, the parser seems to be in an incorrect state and doesn't properly handle subsequent whitespace characters.

### Reproduction

```mdx
<Component
  prop={
    value
  }
/>
```

When parsing JSX tags with line breaks followed by whitespace, the parser doesn't correctly transition between states. This causes the whitespace after newlines to not be properly recognized or consumed.

### Expected behavior

The parser should correctly handle whitespace sequences that follow line endings in JSX expressions. After consuming a line ending, it should properly enter the whitespace state and continue parsing normally.

### Additional context

This seems to affect JSX tags that span multiple lines with indentation. The issue appears to be related to how the parser transitions between handling line endings and whitespace characters in ES/JSX contexts.

---
Repository: /testbed
