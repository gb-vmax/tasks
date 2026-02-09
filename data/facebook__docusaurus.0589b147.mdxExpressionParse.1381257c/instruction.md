# Bug Report

### Describe the bug

I'm experiencing an issue with MDX expression parsing where spread operators in JSX attributes are not being validated correctly. It seems like the parser is allowing multiple properties in spread expressions when it should only permit a single spread.

### Reproduction

```jsx
// This should throw an error but doesn't
<Component {...props} {...moreProps} />

// Single spread works fine
<Component {...props} />
```

When using multiple spread operators in JSX attributes, the parser doesn't catch this as an error. According to MDX specs, only a single spread should be supported in these expressions.

### Expected behavior

The parser should throw an error message like "Unexpected extra content in spread: only a single spread is supported" when multiple spreads are used in a single JSX element.

### Additional context

This appears to be related to how the expression properties are being checked during parsing. The validation logic might not be triggering when it should.

---
Repository: /testbed
