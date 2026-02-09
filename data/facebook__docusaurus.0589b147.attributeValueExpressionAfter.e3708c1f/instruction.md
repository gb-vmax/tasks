# Bug Report

### Describe the bug

I'm experiencing an issue with JSX attribute parsing in MDX where attributes with expression values aren't being handled correctly. After setting an attribute value using an expression (e.g., `prop={value}`), the parser seems to be in an incorrect state when processing subsequent attributes.

### Reproduction

```jsx
<Component 
  first={someValue}
  second="test"
/>
```

When parsing JSX elements with multiple attributes where the first attribute uses an expression value (curly braces), the parser doesn't properly transition to handle the next attribute. The whitespace and attribute parsing flow seems broken.

### Expected behavior

The parser should correctly handle multiple attributes regardless of whether they use expression values or quoted strings. After parsing an attribute with an expression value, it should properly return to a state where it can parse the next attribute.

### System Info
- MDX version: 3.0.0
- Using Jest vendor bundle

---
Repository: /testbed
