# Bug Report

### Describe the bug

I'm encountering an issue with parsing MDX attributes that have quoted values. When using quoted attribute values in JSX tags within MDX content, the closing quote is being included in the attribute value itself instead of being treated as the delimiter.

### Reproduction

```mdx
<Component attr="value" />
```

When parsing this, the attribute value appears to include the closing quote character, resulting in `attr` having the value `"value"` (with quotes) instead of just `value`.

### Expected behavior

The closing quote should be recognized as the end of the attribute value and not be included in the value itself. The attribute value should be `value` without the surrounding quotes.

### Additional context

This seems to affect any JSX-style tags with quoted attribute values in MDX files. The opening quote is handled correctly, but the closing quote is being consumed as part of the value rather than as a delimiter.

---
Repository: /testbed
