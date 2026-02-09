# Bug Report

### Describe the bug

When parsing MDX with quoted attribute values, the parser seems to be exiting the attribute value token at the wrong time. This causes issues with how attribute values are being tokenized in JSX-like syntax.

### Reproduction

```jsx
<Component attribute="value" />
```

When parsing JSX tags with quoted attributes, the tokenizer appears to be handling the attribute value boundaries incorrectly. The issue manifests when the parser encounters quoted strings in attribute values - it's not properly maintaining the token state throughout the entire quoted string.

### Expected behavior

The parser should correctly tokenize the entire quoted attribute value as a single unit before exiting the token state. The attribute value should be fully consumed before the tokenizer moves on to the next state.

### Additional context

This appears to be related to how the `attributeValueQuoted` function handles the token lifecycle. The timing of when tokens are entered and exited during attribute value parsing seems off, which could lead to malformed AST nodes or incorrect parsing results for JSX attributes with quoted values.

---
Repository: /testbed
