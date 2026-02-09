# Bug Report

### Describe the bug

When parsing MDX with JSX attributes that have empty quoted values (like `attr=""`), the parser is producing incorrect syntax tree nodes. The `tagAttributeValueLiteralValueType` node is being created even when there's no actual value between the quotes.

### Reproduction

```jsx
<Component attr="" />
```

When parsing this MDX, the AST includes a `tagAttributeValueLiteralValueType` node that shouldn't exist for empty string values. This causes issues downstream when processing the syntax tree.

### Expected behavior

For empty quoted attribute values, the parser should only create the marker nodes (opening and closing quotes) without creating an intermediate value node, since there is no value content between the quotes.

The correct node structure should have:
- Opening quote marker
- Closing quote marker
- NO value node in between

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
