# Bug Report

### Describe the bug

I'm encountering an issue with JSX attribute parsing where quoted attribute values are not being processed correctly. When using JSX tags with quoted attribute values, the parser seems to exit the attribute value state prematurely, causing the value to be incomplete or incorrectly parsed.

### Reproduction

```jsx
<Component name="value" />
```

When parsing JSX with quoted attributes like the example above, the attribute value doesn't seem to be captured properly. The parser appears to be transitioning states incorrectly when processing the characters inside the quoted string.

### Expected behavior

The parser should:
1. Enter the attribute value state when encountering the opening quote
2. Consume all characters within the quotes
3. Exit the attribute value state only after processing all content and reaching the closing quote

Instead, it seems like the state transitions are happening at the wrong time, which breaks the parsing flow for quoted attribute values.

### Additional context

This appears to affect any JSX element that uses quoted attribute values (both single and double quotes). The issue manifests when the parser is processing the characters between the opening and closing quotes of an attribute value.

---
Repository: /testbed
