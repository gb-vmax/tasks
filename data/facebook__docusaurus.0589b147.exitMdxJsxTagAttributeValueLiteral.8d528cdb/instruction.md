# Bug Report

### Describe the bug

I'm experiencing an issue with JSX attribute parsing in MDX files. When using literal values for JSX attributes, the attribute value is not being set correctly on the last attribute in the attributes array.

### Reproduction

```jsx
// Example MDX file
<Component name="test" value="hello" />
```

When parsing this, the `value` attribute doesn't get assigned properly. Instead of updating the existing attribute object at the correct index, it seems like the value is being placed at an incorrect position in the attributes array.

### Expected behavior

The literal attribute values should be correctly assigned to their corresponding attribute objects in the attributes array. Each attribute should have its `value` property set to the parsed literal string.

### Additional context

This appears to affect how JSX attributes with literal string values (e.g., `attr="value"`) are processed during the markdown-to-AST conversion. The issue might be related to how the attribute array index is calculated when setting the value.

---
Repository: /testbed
