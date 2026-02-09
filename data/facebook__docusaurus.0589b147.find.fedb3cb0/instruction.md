# Bug Report

### Describe the bug

I'm experiencing an issue with data attribute handling in MDX. It seems like data attributes are being processed incorrectly - specifically, the camelCase conversion logic appears to be inverted.

### Reproduction

When using data attributes in MDX components, the attribute names are not being normalized correctly:

```jsx
// Using a data attribute with a dash
<Component data-test-value="hello" />

// Using a data attribute without a dash  
<Component dataTestValue="world" />
```

The attributes are being converted to the wrong format. Attributes that should be converted to camelCase are not being converted, and vice versa.

### Expected behavior

Data attributes should follow the standard HTML data attribute conventions:
- `data-*` attributes with dashes should be properly converted to camelCase when appropriate
- `data*` attributes without dashes should be handled according to the spec

The current behavior seems backwards from what's expected.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
