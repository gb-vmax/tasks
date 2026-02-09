# Bug Report

### Describe the bug

I'm experiencing an issue where function declarations are not being handled correctly in certain scoping scenarios. When a function declaration has an identifier, it seems like the scope resolution is broken, which leads to errors during the build process.

### Reproduction

```js
function myFunction() {
  function innerFunction() {
    // nested function declaration
  }
  innerFunction();
}
```

When bundling code with nested function declarations like the above, I'm getting errors related to variable scope resolution. The function identifier appears to not be properly registered in the correct scope.

This seems to happen specifically with:
- Named function declarations
- Nested functions inside other functions
- Functions that are called within the same scope they're declared

### Expected behavior

Function declarations should be properly scoped and their identifiers should be accessible within their containing scope. The bundler should be able to resolve the function name without errors.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
