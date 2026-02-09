# Bug Report

### Describe the bug

I'm experiencing an issue with token context handling in MDX parsing. It appears that the `preserveSpace` and `generator` properties are being set incorrectly in certain contexts, which is causing unexpected behavior when parsing MDX content.

### Reproduction

When processing MDX files with specific token contexts, the parser seems to be using the wrong values for space preservation and generator flags. This affects how whitespace and generator functions are handled during parsing.

```js
// Example MDX content that triggers the issue
const mdxContent = `
{/* Some JSX expression */}
<Component>
  Content with specific spacing
</Component>
`;

// The token context is created with incorrect property assignments
// preserveSpace ends up with the value from isExpr instead of preserveSpace parameter
// generator ends up with the value from override instead of generator parameter
```

### Expected behavior

The `TokContext` constructor should correctly assign:
- `preserveSpace` based on the `preserveSpace` parameter
- `generator` based on the `generator` parameter

Instead, it appears these values are being swapped or assigned from the wrong parameters, leading to incorrect parsing behavior for whitespace handling and generator detection.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it might be a regression from a recent change. The token context properties don't match what's being passed to the constructor.

---
Repository: /testbed
