# Bug Report

### Describe the bug

I'm encountering an issue with MDX attribute parsing where the parser seems to be entering an incorrect state after processing expression attribute values. The code appears to be calling `esWhitespaceStart` recursively or setting it as a return state, which doesn't seem right.

### Reproduction

```mdx
<Component 
  prop1={someValue}
  prop2="test"
/>
```

When parsing MDX components with expression-based attribute values (using `{}`), the parser behavior becomes unpredictable. It seems like the state machine is not transitioning correctly after processing the expression.

### Expected behavior

After parsing an attribute value expression, the parser should properly exit the attribute type state and transition to the `attributeBefore` state to handle the next attribute or the closing tag. The whitespace handling should work as expected without causing state confusion.

### Additional context

This appears to be related to how the `attributeValueExpressionAfter` function handles state transitions. The current implementation seems to be mixing up return states and effect exits in a way that could cause the parser to get stuck or behave incorrectly.

---
Repository: /testbed
