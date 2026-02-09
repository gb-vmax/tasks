# Bug Report

### Describe the bug

I'm encountering an issue with named function expressions where the function name identifier is not being properly handled. When a function expression has a name, it seems like the name is not being parsed or registered correctly in the scope.

### Reproduction

```js
const fn = function myFunction() {
  // myFunction should be accessible here
  console.log(myFunction);
};
```

When using named function expressions like the above, the function name identifier doesn't seem to be getting parsed properly. This affects scenarios where the function needs to reference itself recursively or when debugging.

### Expected behavior

Named function expressions should have their identifier properly parsed and available within the function scope. The function name should be accessible inside the function body for recursive calls or other purposes.

### Additional context

This appears to be related to how function expression identifiers are being checked during the parsing phase. The issue manifests when trying to use the function name within its own body.

---
Repository: /testbed
