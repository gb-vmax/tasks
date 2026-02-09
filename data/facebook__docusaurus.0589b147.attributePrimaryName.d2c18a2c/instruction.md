# Bug Report

### Describe the bug

JSX attribute parsing is failing when attribute names contain the `=` character (code 61). The parser crashes instead of properly handling attributes with equals signs in their names.

### Reproduction

```jsx
<Component attribute=value />
```

When parsing MDX content with JSX attributes that have `=` in the attribute name position, the parser throws an error instead of treating it as the start of the attribute value assignment.

### Expected behavior

The parser should recognize `=` (code 61) as a valid transition point from the attribute name to the attribute value, not as part of the attribute name itself. The attribute should be parsed correctly and the component should render without errors.

### Additional context

This appears to affect basic JSX attribute syntax. The issue occurs during the attribute name parsing phase where the parser needs to distinguish between the attribute name and the assignment operator.

---
Repository: /testbed
