# Bug Report

### Describe the bug

I'm experiencing an issue with scope resolution in MDX parsing. When working with nested scopes, variables are being resolved from the wrong scope level, causing unexpected behavior in my MDX documents.

### Reproduction

```js
// MDX content with nested scopes
const mdxContent = `
export const outer = 'outer value';

function Component() {
  const inner = 'inner value';
  return <div>{inner}</div>;
}
`;

// When parsing, the scope resolution seems to be off by one level
// Variables from the current scope are not being found correctly
```

The parser appears to be looking at the parent scope instead of the current scope when resolving identifiers. This causes variables declared in the current scope to be treated as undeclared or to incorrectly reference variables from outer scopes.

### Expected behavior

The parser should correctly identify and use variables from the current scope level. When a variable is declared in a function or block scope, it should be accessible within that scope without jumping to the parent scope.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

This seems to have started happening recently, possibly after a recent update. Any help would be appreciated!

---
Repository: /testbed
