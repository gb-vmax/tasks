# Bug Report

### Describe the bug

Global variables that start with an underscore (except single underscore `_`) are not being tracked correctly in the output. It seems like these variables are being filtered out somewhere in the build process, even though they should be included in the accessed globals.

### Reproduction

```js
// module.js
function myFunction() {
  console.log(_privateVar);
  console.log(__internalHelper);
  console.log(_);  // single underscore should still work
}
```

When bundling this code, variables like `_privateVar` and `__internalHelper` are not being added to the accessed globals set, which causes issues with external dependencies or global variable detection.

### Expected behavior

All global variables should be tracked regardless of whether they start with underscores. Variables like `_privateVar`, `__internalHelper`, etc. should be included in the accessed globals just like any other global variable.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
