# Bug Report

### Describe the bug

I'm experiencing an issue with variable scope resolution in MDX parsing. When declaring variables in nested scopes, the parser seems to be skipping the current scope and starting from the parent scope instead. This causes incorrect scope lookups and can lead to variables not being found when they should be accessible.

### Reproduction

```js
// Example MDX content with nested scopes
{
  var x = 1;
  {
    var y = 2;
    // Variable lookup here fails to check the immediate scope
  }
}
```

The parser appears to be starting its scope search from the wrong position in the scope stack, causing it to miss variables defined in the current var scope.

### Expected behavior

The parser should search through all relevant scopes starting from the current one, not skip the current scope when looking for variable declarations. Variable lookups should find declarations in the immediate scope before checking parent scopes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
