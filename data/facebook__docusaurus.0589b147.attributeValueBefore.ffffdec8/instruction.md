# Bug Report

### Describe the bug

When using curly braces `{}` in MDX attribute values, the parser is treating them as literal string values instead of JavaScript expressions. This causes the attribute value to be interpreted incorrectly.

### Reproduction

```mdx
<Component prop={someValue} />
```

The value `{someValue}` should be parsed as a JavaScript expression, but instead it's being treated as a quoted literal string similar to `"value"` or `'value'`.

### Expected behavior

Curly braces in attribute values should trigger expression parsing, not literal value parsing. The parser should recognize `{` as the start of a JavaScript expression and handle it accordingly.

### Additional context

This appears to affect how MDX components receive props - instead of getting the evaluated JavaScript value, they're receiving the raw string representation.

---
Repository: /testbed
