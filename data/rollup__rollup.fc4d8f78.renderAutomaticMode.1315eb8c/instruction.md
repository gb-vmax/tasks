# Bug Report

### Describe the bug

When using JSX elements in automatic mode with attributes but no children, the generated code is malformed. The attributes object is not being properly closed/wrapped, resulting in invalid JavaScript output.

### Reproduction

```jsx
// JSX input
<Component foo="bar" />

// Expected output (simplified):
jsxs(Component, { foo: "bar" })

// Actual output:
// Malformed - attributes object not properly handled
```

This happens specifically when:
1. Using JSX in automatic runtime mode
2. Element has attributes
3. Element has NO children (self-closing or empty)

The issue seems to affect the code generation phase where attributes are being wrapped. When there are attributes but no children, the wrapping logic doesn't execute correctly.

### Expected behavior

Self-closing JSX elements with attributes should generate valid JavaScript code with properly formatted props object, regardless of whether children are present or not.

### System Info
- Rollup version: latest
- JSX runtime: automatic mode

---
Repository: /testbed
