# Bug Report

### Describe the bug

I'm experiencing an issue with JSX attribute parsing in MDX files. When using multiple JSX attributes on a component, the attribute names are being assigned to the wrong attributes in the parsed output.

### Reproduction

```jsx
<Component 
  firstAttr="value1"
  secondAttr="value2"
/>
```

When parsing the above MDX, the attribute names get mixed up - it seems like `secondAttr` is being assigned to the first attribute instead of the second one.

### Expected behavior

Each attribute name should be correctly assigned to its corresponding attribute object in the order they appear. The first attribute should have the name `firstAttr` and the second should have `secondAttr`.

### Additional context

This appears to affect components with multiple attributes. Single attribute components seem to work fine. The issue seems related to how the parser indexes into the attributes array when setting the name property.

---
Repository: /testbed
