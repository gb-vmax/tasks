# Bug Report

### Describe the bug

I'm experiencing an issue with scope resolution in MDX parsing. When parsing MDX content, variables declared in the current scope are not being recognized properly, leading to incorrect scope lookups.

### Reproduction

```js
// Example MDX content that triggers the issue
export const myVar = 'test';

function MyComponent() {
  const localVar = 'local';
  return <div>{localVar}</div>;
}
```

When parsing this MDX, the scope resolution seems to be looking at the wrong scope level. Variables that should be accessible in the current scope are being treated as if they're in a parent scope instead.

### Expected behavior

The parser should correctly identify and resolve variables in the current scope. When checking `currentScope()`, it should return the actual current scope where variables are being declared/accessed, not a parent or undefined scope.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This is causing issues with variable resolution in our MDX documents where locally scoped variables are not being found correctly.

---
Repository: /testbed
