# Bug Report

### Describe the bug
When using directives with attributes in remark-directive, the attribute values are being assigned to the wrong attribute. The value from one attribute ends up being set on a different attribute than expected.

### Reproduction
```js
// Parse markdown with directive that has multiple attributes
const markdown = ':directive[text]{attr1="value1" attr2="value2"}'

// After parsing, the attributes are incorrectly mapped
// Expected: attr1="value1", attr2="value2"
// Actual: attr2 gets value1, or similar incorrect mapping
```

### Expected behavior
Each attribute should receive its own corresponding value. When parsing directives with multiple attributes, the attribute-value pairs should be correctly associated with each other.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
