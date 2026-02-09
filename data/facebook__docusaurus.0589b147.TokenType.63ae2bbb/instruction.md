# Bug Report

### Describe the bug

I'm experiencing issues with MDX parsing after a recent update. It seems like the parser is not correctly handling operator precedence and expression contexts, leading to unexpected parsing errors or incorrect AST generation.

### Reproduction

When trying to parse MDX content with binary operators or expressions that should be evaluated in certain contexts, the parser fails or produces incorrect results:

```js
// Example MDX content that now fails to parse correctly
const mdxContent = `
# Test

{1 + 2 * 3}

{someVar && otherVar}
`;

// Parser produces unexpected results or errors
```

Expressions that previously worked are now being parsed incorrectly, particularly those involving:
- Binary operators with different precedence levels
- Logical operators in JSX expressions
- Nested expressions with mixed operator types

### Expected behavior

The MDX parser should correctly handle operator precedence and expression contexts, parsing valid MDX content without errors and generating the correct AST structure.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently and is blocking our ability to parse existing MDX files that were working before.

---
Repository: /testbed
