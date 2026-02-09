# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where whitespace handling after line endings in JSX expressions appears to be broken. When there's a newline followed by whitespace in JSX attribute values or expressions, the parser seems to be consuming tokens incorrectly or getting into an invalid state.

### Reproduction

```mdx
<Component
  prop="value"
  anotherProp={
    someExpression
  }
/>
```

When parsing MDX content with JSX tags that have line breaks followed by whitespace (like indentation), the parser doesn't handle the whitespace correctly. It seems like after processing a line ending, the subsequent whitespace isn't being consumed properly.

### Expected behavior

The parser should correctly handle whitespace that follows line endings in JSX expressions and attributes. The MDX content should parse without errors and maintain proper token flow.

### Additional context

This seems to affect JSX tags with multi-line attributes or expressions. Single-line JSX works fine, but as soon as you introduce line breaks with indentation, the parsing behavior changes unexpectedly.

---
Repository: /testbed
