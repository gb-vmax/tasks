# Bug Report

### Describe the bug

I'm experiencing an issue where global variables are not being reused correctly across the codebase. It seems like every time a global variable is accessed, a new instance is being created instead of returning the existing one.

### Reproduction

```js
// First access to a global variable
const var1 = scope.findVariable('myGlobal');

// Second access to the same global variable
const var2 = scope.findVariable('myGlobal');

// These should be the same instance, but they're not
console.log(var1 === var2); // Expected: true, Actual: false
```

### Expected behavior

When calling `findVariable()` multiple times with the same variable name, it should return the same `GlobalVariable` instance. The scope should maintain a single instance per variable name and reuse it on subsequent lookups.

### Additional context

This is causing issues with variable tracking and analysis in my build. Each reference to the same global variable is being treated as a completely separate entity, which breaks dependency tracking and leads to incorrect build outputs.

---
Repository: /testbed
