# Bug Report

### Describe the bug

I'm experiencing an issue with parsing JSX/MDX attributes that have quoted values. When an attribute has a quoted string value, the parser seems to be exiting the value state prematurely and not consuming all the characters in the quoted string properly.

### Reproduction

```jsx
<Component attr="value" />
```

When parsing JSX tags with quoted attribute values like the example above, the attribute value parsing doesn't work as expected. The parser appears to exit the literal value type before processing the actual content of the quoted string.

### Expected behavior

The parser should:
1. Enter the quoted attribute value state
2. Consume all characters within the quotes
3. Exit the value state only after reaching the closing quote or end of input
4. Properly handle the complete quoted string as the attribute value

### Additional context

This affects any JSX/MDX code that uses quoted attribute values (both single and double quotes). The issue seems to be in the `attributeValueQuoted` function where the state transitions aren't happening in the correct order.

---
Repository: /testbed
