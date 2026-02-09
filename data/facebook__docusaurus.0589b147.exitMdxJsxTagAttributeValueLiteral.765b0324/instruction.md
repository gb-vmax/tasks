# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX attribute parsing where attribute values are being assigned to the wrong attributes. When parsing JSX tags with multiple attributes, the literal values seem to be getting attached to the incorrect attribute in the array.

### Reproduction

```mdx
<Component 
  firstAttr="value1"
  secondAttr="value2"
/>
```

When this gets parsed, `"value2"` ends up being assigned to `firstAttr` instead of `secondAttr`. It seems like the parser is looking at the wrong index when setting attribute values.

### Expected behavior

Each attribute value should be correctly assigned to its corresponding attribute name. In the example above:
- `firstAttr` should have value `"value1"`
- `secondAttr` should have value `"value2"`

### Additional context

This appears to affect JSX tags with literal attribute values. The issue doesn't occur with single attributes, only when there are multiple attributes on the same component.

---
Repository: /testbed
