# Bug Report

### Describe the bug

I'm experiencing an issue with parsing JSX/MDX attributes that have quoted values. When an attribute value is enclosed in quotes and contains certain characters, the parser seems to get stuck in an infinite loop or doesn't properly close the attribute value parsing state.

### Reproduction

```jsx
<Component attr="some value" />
```

When trying to parse MDX content with quoted attribute values like the above, the parser doesn't seem to handle the closing quote correctly. The issue appears to be related to how the state machine transitions when exiting the quoted attribute value.

### Expected behavior

The parser should correctly handle quoted attribute values and properly transition through parsing states:
1. Enter the quoted value state
2. Consume characters within the quotes
3. Exit the quoted value state when encountering the closing quote
4. Continue parsing the rest of the tag

Instead, it seems like the state transitions are happening in the wrong order, which causes the parser to not properly close out the attribute value parsing.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
