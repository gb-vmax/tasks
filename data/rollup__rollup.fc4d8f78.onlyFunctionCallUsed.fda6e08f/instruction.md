# Bug Report

### Describe the bug

I'm experiencing an issue with function declarations that are only used in call expressions. When a function is defined and only called (never passed around or assigned), the tree-shaking behavior seems incorrect.

### Reproduction

```js
// Function defined in a variable declarator
const myFunction = function() {
  console.log('side effect');
  return 42;
};

// Only used as function call
myFunction();
```

The function should be treated differently when it's only invoked directly versus when it's passed around as a value. Currently, it seems like functions that aren't assigned to variables (or in certain declaration contexts) are being handled incorrectly.

### Expected behavior

Functions that are only used in direct call expressions should be properly identified and optimized accordingly. The analysis should correctly determine whether a function is only used via function calls or if it's also used as a value.

### Additional context

This seems related to how the parent node type is checked when determining function call usage patterns. The issue appears when the function is not in a `VariableDeclarator` context.

---
Repository: /testbed
