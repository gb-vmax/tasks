# Bug Report

### Describe the bug

I'm encountering an issue with parsing JSX/MDX attribute values that contain quoted strings. When an attribute has a quoted value (like `prop="value"`), the parser seems to be consuming the closing quote character incorrectly, which leads to unexpected parsing behavior.

### Reproduction

```jsx
<Component prop="some value" />
```

When parsing JSX tags with quoted attribute values, the closing quote is being consumed before the parser properly exits the value state. This causes the parser to lose track of where the attribute value ends.

### Expected behavior

The parser should:
1. Read the opening quote
2. Consume all characters in the attribute value
3. Exit the attribute value state
4. Then consume the closing quote
5. Continue parsing the rest of the tag

Instead, it appears to be consuming the closing quote while still in the value state, which breaks the parsing flow.

### Additional context

This affects any JSX/MDX syntax where attributes use quoted values. The issue is specifically in the `attributeValueQuoted` function where the state transitions aren't happening in the correct order.

---
Repository: /testbed
