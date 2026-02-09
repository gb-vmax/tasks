# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX attribute value expressions where the estree data is not being attached correctly to attribute nodes. When parsing JSX attributes with expression values in MDX files, the resulting AST seems to have missing or incorrect estree metadata.

### Reproduction

```jsx
// Example MDX file with JSX attribute expression
<Component attribute={someExpression} />
```

When parsing this, the attribute value expression node should contain the estree data when available, but it appears to be missing or attached to the wrong attribute in the parsed output.

### Expected behavior

The `mdxJsxAttributeValueExpression` node should have its `data.estree` property properly set when the estree token data is present. The estree metadata should be attached to the correct attribute in the attributes array.

### Additional context

This seems to be affecting how MDX processes JSX attribute expressions. The parsed AST structure doesn't match what's expected for proper transformation of these expressions.

---
Repository: /testbed
