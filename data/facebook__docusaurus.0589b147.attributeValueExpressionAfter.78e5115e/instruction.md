# Bug Report

### Describe the bug

I'm experiencing an issue with MDX attribute parsing where the attribute value expression handler exits the tag attribute type before calling the whitespace parser. This causes the state machine to be in an incorrect state when processing whitespace after JSX expression attributes.

### Reproduction

```jsx
<Component
  attr={someValue}
  nextAttr="value"
/>
```

When parsing MDX with JSX expression attributes (using `{}`), the parser doesn't handle the whitespace correctly after the closing brace. The attribute type is exited too early in the state machine flow.

### Expected behavior

The parser should properly handle whitespace after expression attributes and correctly transition to the next attribute parsing state. The attribute type should only be exited after the whitespace parsing completes.

### Additional context

This appears to be related to the order of operations in `attributeValueExpressionAfter` - the function should call `esWhitespaceStart` and capture its result before modifying the parser state (exiting the tag attribute type and setting the return state).

---
Repository: /testbed
