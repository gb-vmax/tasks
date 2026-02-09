# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where parenthesized expressions are not being handled correctly. It seems like the parser is removing parentheses from expressions that should keep them, or possibly applying transformations to the wrong nodes in the AST.

### Reproduction

```jsx
const mdx = `
export const value = (someExpression);

<Component prop={(x) => x} />
`;

// Parse the MDX
const result = compile(mdx);
// The parenthesized expressions are being incorrectly transformed
```

### Expected behavior

Parenthesized expressions should be preserved or handled correctly during the AST transformation. The current behavior seems to be applying the `esnode.expression` replacement to nodes that shouldn't be transformed, or skipping nodes that should be transformed.

### Additional context

This appears to affect how the MDX compiler processes JavaScript expressions wrapped in parentheses. The issue might be related to how the AST visitor is checking node types and applying transformations.

---
Repository: /testbed
