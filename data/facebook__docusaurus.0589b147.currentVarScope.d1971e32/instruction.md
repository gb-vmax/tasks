# Bug Report

### Describe the bug

I'm experiencing an issue with variable scope resolution in MDX parsing. When using `var` declarations inside nested scopes (like blocks or functions), the variables aren't being resolved to the correct scope level. This seems to be causing the parser to return the wrong scope context.

### Reproduction

```js
function example() {
  {
    var x = 1;
  }
  // x should be accessible here due to var hoisting
  console.log(x);
}
```

When parsing this code with MDX, the scope resolution appears to be off. The `var` declaration should hoist to the function scope, but it seems like the parser is looking at the wrong scope level.

### Expected behavior

Variables declared with `var` should be resolved to their proper function or global scope, not the immediate block scope. The `currentVarScope()` method should traverse the scope stack correctly and find the first scope that allows `var` declarations.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This might be related to how the scope stack is being traversed. Any help would be appreciated!

---
Repository: /testbed
