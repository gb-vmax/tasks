# Bug Report

### Describe the bug

I'm experiencing an issue with MDX attribute value expressions where the parser seems to be handling the state transitions incorrectly. When using JSX-style expression attributes (like `<Component prop={value} />`), the parser appears to be exiting the wrong token type before processing whitespace.

### Reproduction

```mdx
<MyComponent 
  value={someExpression}
  otherProp="test"
/>
```

When parsing MDX files with expression-based attribute values, the token exit happens at the wrong point in the parsing flow. This seems to affect how the parser handles the transition from the attribute value expression back to processing subsequent attributes.

### Expected behavior

The parser should correctly exit the `tagAttributeValueExpressionType` token after processing an attribute value expression, and then handle any whitespace before moving to the next attribute. The state should be properly set before processing whitespace to ensure correct parsing flow.

### Additional context

This appears to be related to the order of operations when exiting token types and setting return states in the attribute value expression handler. The issue manifests when you have multiple attributes where at least one uses an expression value.

---
Repository: /testbed
