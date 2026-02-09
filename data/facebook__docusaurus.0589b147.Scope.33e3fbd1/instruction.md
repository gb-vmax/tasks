# Bug Report

### Describe the bug

I'm experiencing an issue with variable scoping in the MDX parser. It appears that lexical scope declarations are being incorrectly shared with var scope, causing variables to leak across scopes when they shouldn't.

### Reproduction

When parsing MDX content with block-scoped variables (let/const) and function-scoped variables (var), the lexical scope seems to be referencing the same array as the var scope instead of maintaining separate scopes.

```js
// Example MDX content that triggers the issue
const mdxContent = `
{(() => {
  let blockScoped = 'test';
  var functionScoped = 'test2';
  return null;
})()}
`;

// Parse the MDX
// The lexical and var scopes are now pointing to the same array
// This causes block-scoped variables to be treated as function-scoped
```

### Expected behavior

Lexical scope (for let/const) and var scope should be maintained separately. Block-scoped variables should not leak into the parent scope like function-scoped variables do.

The parser should correctly distinguish between:
- Variables declared with `let`/`const` (lexical scope)
- Variables declared with `var` (function scope)

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems like a regression as the scopes were previously handled separately with distinct arrays.

---
Repository: /testbed
