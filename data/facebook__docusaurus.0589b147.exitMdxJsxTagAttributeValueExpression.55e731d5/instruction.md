# Bug Report

### Describe the bug

When using MDX JSX tags with multiple attributes that have expression values, only the first attribute gets the expression value assigned correctly. All subsequent attributes with expression values are being incorrectly assigned to the tag itself rather than to their respective attributes.

### Reproduction

```mdx
<Component 
  first={value1}
  second={value2}
  third={value3}
/>
```

When parsing this MDX, the expression values for `second` and `third` attributes are not being set on the correct attribute objects. Instead of each attribute having its own expression value, something goes wrong with how the values are being assigned.

### Expected behavior

Each attribute should have its expression value properly assigned to it. The parsed AST should show:
- `first` attribute with value `{value1}`
- `second` attribute with value `{value2}` 
- `third` attribute with value `{value3}`

Instead, it seems like only the first attribute is getting its value set correctly, while the others are being handled incorrectly.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
