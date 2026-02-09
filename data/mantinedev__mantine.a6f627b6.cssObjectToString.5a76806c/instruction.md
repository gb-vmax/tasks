# Bug Report

### Describe the bug
When using inline styles with `undefined` values, the generated CSS string includes malformed properties. The CSS output contains property names with colons but no values, resulting in invalid CSS syntax like `property-name:` instead of properly omitting the property.

### Reproduction
```jsx
const styles = {
  color: 'red',
  backgroundColor: undefined,
  fontSize: '16px'
}

// The generated CSS string incorrectly includes "background-color:"
// Expected: "color:red;font-size:16px;"
// Actual: "color:red;background-color:font-size:16px;"
```

### Expected behavior
Properties with `undefined` values should be completely omitted from the generated CSS string, not included as malformed properties.

### System Info
- Mantine version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
