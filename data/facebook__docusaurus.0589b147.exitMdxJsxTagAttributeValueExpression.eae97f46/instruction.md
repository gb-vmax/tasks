# Bug Report

### Describe the bug

When using JSX attribute expressions in MDX files, the attribute value is being assigned to the wrong attribute. It seems like the value expression is being attached to the second-to-last attribute instead of the last one.

### Reproduction

```mdx
<Component 
  first="value1"
  second={expression}
/>
```

In this case, the expression `{expression}` ends up being assigned to the `first` attribute instead of the `second` attribute where it should be.

### Expected behavior

The attribute value expression should be assigned to the correct (last) attribute that it corresponds to. In the example above, `{expression}` should be the value of the `second` attribute, not the `first` attribute.

### Additional context

This appears to affect any JSX tags with multiple attributes where at least one uses an expression value. The issue manifests as attribute values being misaligned with their corresponding attribute names.

---
Repository: /testbed
