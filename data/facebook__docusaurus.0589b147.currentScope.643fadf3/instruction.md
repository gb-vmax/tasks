# Bug Report

### Describe the bug

I'm experiencing an issue with scope resolution in the MDX parser. When working with nested scopes, the parser seems to be returning the wrong scope level, which is causing variables to be resolved incorrectly.

### Reproduction

```js
// Example MDX content with nested scopes
const mdxContent = `
export const outer = 'outer value';

function Component() {
  const inner = 'inner value';
  
  return <div>{inner}</div>;
}
`;

// When parsing this, the scope resolution appears to skip a level
// Variables that should be found in the current scope are not being detected properly
```

### Expected behavior

The `currentScope()` method should return the actual current scope (the topmost scope in the stack). Variables declared in the current scope should be accessible and properly resolved.

### Actual behavior

It seems like the scope being returned is one level up from where it should be, causing the parser to look in the wrong scope for variable declarations. This leads to incorrect variable resolution and potential scoping errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
