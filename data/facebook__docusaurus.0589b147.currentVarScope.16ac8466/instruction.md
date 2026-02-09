# Bug Report

### Describe the bug

I'm encountering an issue with variable scope resolution in MDX parsing. It appears that the current variable scope is being incorrectly determined, causing variables to be resolved in the wrong scope context.

### Reproduction

When parsing MDX content with nested scopes (like functions inside blocks), the variable scope lookup seems to skip the current scope and starts checking from the parent scope instead. This leads to incorrect variable resolution behavior.

Example scenario:
```js
// MDX content with nested scopes
function outer() {
  var x = 1;
  {
    var y = 2;
    // Variable lookup here incorrectly skips the immediate scope
  }
}
```

The scope resolution starts from the wrong position in the scope stack, potentially missing variables declared in the current scope level.

### Expected behavior

The `currentVarScope()` function should traverse the scope stack starting from the current scope (top of the stack) and find the nearest variable scope, not skip the current scope entirely.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
