# Bug Report

### Describe the bug

I'm experiencing an issue with scope handling in nested blocks. When declaring variables in child scopes, they seem to be sharing declaration maps with their parent scopes instead of maintaining separate ones. This causes variable declarations to leak between scopes incorrectly.

### Reproduction

```js
function example() {
  let x = 1;
  
  {
    let y = 2; // This should be in child scope only
    console.log(x); // Should access parent scope
  }
  
  // y should not be accessible here, but it appears in the declarations
}
```

When analyzing the scope structure:
1. Create a parent scope with some declarations
2. Create a child block scope
3. Add declarations to the child scope
4. The child scope's declarations map appears to be the same reference as the parent's

This means variables declared in child scopes are being added to the parent scope's declaration map, breaking proper scope isolation.

### Expected behavior

Each scope should maintain its own separate declarations map. Child scopes should be able to look up parent declarations but should not share the same underlying Map object. Variable declarations in a child scope should not affect the parent scope's declarations.

### Additional context

This seems to have started happening recently. The scope chain traversal for variable lookups should still work, but the declaration storage needs to be independent per scope level.

---
Repository: /testbed
