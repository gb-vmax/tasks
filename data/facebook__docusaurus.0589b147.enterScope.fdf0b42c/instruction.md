# Bug Report

### Describe the bug

I'm experiencing an issue with scope management in the MDX parser. When parsing MDX content with nested scopes (like functions inside functions or nested blocks), the parser seems to lose track of inner scopes and only maintains the outermost scope.

### Reproduction

```js
const mdxContent = `
export function outer() {
  function inner() {
    const x = 1;
  }
}
`;

// Parse the MDX content
const result = parseMDX(mdxContent);
// Inner function scope is not properly tracked
```

This affects any MDX content with nested structures like:
- Nested function declarations
- Nested block statements
- Nested class methods

### Expected behavior

The parser should maintain a proper stack of scopes, allowing for multiple nested levels. Each call to `enterScope` should add a new scope to the stack, not just initialize it once.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
