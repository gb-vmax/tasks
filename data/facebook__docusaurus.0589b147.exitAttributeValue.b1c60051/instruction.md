# Bug Report

### Describe the bug

I'm experiencing an issue with directive attribute parsing where the attribute values are being assigned to the wrong attribute name. When using directives with multiple attributes, the value gets assigned to the previous attribute instead of the current one.

### Reproduction

```markdown
::directive{attr1="value1" attr2="value2"}
content
::
```

When parsing this directive, `value2` ends up being assigned to `attr1` instead of `attr2`. The attribute-value pairing is off by one.

### Expected behavior

Each attribute value should be correctly paired with its corresponding attribute name. In the example above:
- `attr1` should have value `"value1"`
- `attr2` should have value `"value2"`

Instead, what's happening is the values are being assigned to the wrong attributes.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
