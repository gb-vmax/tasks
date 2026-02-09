# Bug Report

### Describe the bug

I'm encountering an issue with MDX attribute parsing where quoted attribute values are not being handled correctly. When parsing JSX-like tags with quoted attributes, the parser seems to consume characters incorrectly, leading to malformed output or parsing errors.

### Reproduction

```jsx
<Component attr="value with spaces" />
```

When this gets parsed, the quoted attribute value doesn't seem to be processed properly. The issue appears to be related to how the parser handles the content between quotes in attribute values.

### Expected behavior

The parser should correctly handle quoted attribute values, including:
- Preserving all content between the opening and closing quotes
- Properly recognizing when the closing quote is reached
- Handling edge cases like empty strings or values with special characters

The attribute value should be fully captured before moving to the next parsing state.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
