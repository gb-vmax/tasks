# Bug Report

### Describe the bug

I'm experiencing an issue with MDX expression parsing where certain edge cases with tokens at boundary positions are not being handled correctly. When working with expressions that have tokens exactly at the prefix or suffix boundaries, they seem to be getting incorrectly filtered out or included.

### Reproduction

```js
// Example with an expression that has tokens at exact boundary positions
const mdxExpression = '{value}';

// When parsing, tokens that should be included/excluded at boundaries
// are being processed incorrectly
```

The problem appears to be related to how token positions are checked against the prefix and suffix lengths. Tokens that are exactly at the boundary (where `token.end === prefix.length` or `token.start - prefix.length === source.length`) are being handled inconsistently.

### Expected behavior

Tokens at exact boundary positions should be consistently included or excluded based on whether they are actually part of the source content. The current logic seems to have off-by-one issues when checking these boundaries.

### Additional context

This is affecting MDX code blocks and expressions that have content right at the edges of the parsed region. The issue is subtle but can cause valid expressions to be incorrectly processed or filtered.

---
Repository: /testbed
