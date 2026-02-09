# Bug Report

### Describe the bug

When parsing MDX with JSX attributes that have expression values followed by whitespace, the parser seems to be processing the whitespace before setting the correct return state. This causes issues with attribute parsing in certain edge cases.

### Reproduction

```jsx
<Component
  prop={value}
  anotherProp="test"
/>
```

When the expression value `{value}` is followed by whitespace and then another attribute, the parser doesn't correctly transition back to the attribute parsing state. The order of operations appears to be incorrect - the whitespace is being consumed before the return state is properly set.

### Expected behavior

The parser should correctly handle the transition from expression values to subsequent attributes, regardless of whitespace. The return state should be set before processing whitespace to ensure proper state management.

### System Info
- remark-mdx version: 3.0.0
- Parser: acorn-based JSX parser

---
Repository: /testbed
