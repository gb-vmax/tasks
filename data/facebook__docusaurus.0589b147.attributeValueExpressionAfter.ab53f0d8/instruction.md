# Bug Report

### Describe the bug

I'm experiencing an issue with MDX attribute parsing where the return state is being set after calling `esWhitespaceStart()` instead of before. This causes the parser to potentially use an incorrect return state when processing whitespace after attribute value expressions.

### Reproduction

```jsx
<Component
  prop={expression}
  anotherProp="value"
/>
```

When parsing JSX attributes with expression values followed by other attributes, the parser's state management appears to be out of order. The `returnState` is being assigned after the whitespace handler is invoked, which could lead to the wrong state being used during parsing.

### Expected behavior

The return state should be set before calling the whitespace handler so that when the parser returns from processing whitespace, it knows the correct state to transition to (in this case, `attributeBefore`).

### System Info
- MDX version: 3.0.0
- Parser: @mdx-js/mdx

This seems like it could cause subtle parsing issues when attributes with expression values are followed by additional attributes or whitespace. Has anyone else encountered this?

---
Repository: /testbed
