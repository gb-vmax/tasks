# Bug Report

### Describe the bug

I'm encountering an issue with scope resolution in the MDX parser. When parsing MDX files with nested scopes (like functions inside blocks), the parser seems to be returning incorrect scope information or hanging indefinitely.

### Reproduction

```js
const mdx = `
function outer() {
  var x = 1;
  function inner() {
    var y = 2;
    return x + y;
  }
  return inner();
}
`;

// Parsing this MDX content causes unexpected behavior
// The parser either hangs or returns incorrect scope data
```

### Expected behavior

The parser should correctly identify and return the appropriate variable scope when traversing nested function scopes. Variable declarations should be properly resolved to their containing scope.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to affect any MDX content with nested function scopes or block-level variable declarations. The issue appears to be in the scope stack traversal logic.

---
Repository: /testbed
