# Bug Report

### Describe the bug

I'm experiencing an issue where the first parameter in a function isn't being marked as reassigned when it should be. This is causing incorrect behavior in my code analysis/bundling workflow.

### Reproduction

```js
function example(firstParam, secondParam) {
  firstParam = 'modified';
  secondParam = 'also modified';
  return firstParam + secondParam;
}
```

In the above code, both `firstParam` and `secondParam` are reassigned, but only `secondParam` seems to be detected as reassigned. The first parameter is being skipped somehow.

### Expected behavior

All parameters that are reassigned within a function body should be properly marked as reassigned, including the first parameter. Currently it seems like only parameters starting from the second one are being tracked correctly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
