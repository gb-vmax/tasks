# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX attribute parsing where literal attribute values are being assigned to the wrong attribute in the attributes array. When parsing JSX tags with multiple attributes, the literal value appears to be applied to the second-to-last attribute instead of the last one.

### Reproduction

```jsx
<Component 
  firstAttr="value1"
  secondAttr="value2"
/>
```

When parsing the above MDX JSX, the literal value `"value2"` gets assigned to `firstAttr` instead of `secondAttr`.

This seems to affect any JSX tag with multiple attributes where at least one has a literal string value.

### Expected behavior

Literal attribute values should be assigned to the correct (last) attribute in the attributes array, not the second-to-last one. The parser should correctly match each attribute name with its corresponding value.

### Additional context

This appears to be related to how `exitMdxJsxTagAttributeValueLiteral` handles the attributes array indexing. The issue manifests when processing MDX files with JSX components that have multiple props.

---
Repository: /testbed
