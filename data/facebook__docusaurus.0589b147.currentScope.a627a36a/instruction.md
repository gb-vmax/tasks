# Bug Report

### Describe the bug

I'm experiencing an issue with scope resolution in the MDX parser. When declaring variables or functions in nested scopes, the parser seems to be looking at the wrong scope level, causing unexpected behavior with variable declarations and references.

### Reproduction

```js
function outer() {
  const x = 1;
  
  function inner() {
    const y = 2;
    // Variable references here are resolved incorrectly
    return x + y;
  }
  
  return inner();
}
```

When parsing MDX content with nested function scopes or block scopes, the current scope being checked appears to be off by one level. This causes issues with:
- Variable shadowing not working as expected
- Incorrect scope resolution for identifiers
- False positives/negatives in local export checking

### Expected behavior

The parser should correctly identify the current scope level and resolve variables according to JavaScript scoping rules. Nested scopes should be handled properly with each level maintaining its own variable bindings.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it might be related to how the scope stack is being accessed in the parser internals.

---
Repository: /testbed
