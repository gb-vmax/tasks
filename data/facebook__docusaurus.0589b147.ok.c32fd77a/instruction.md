# Bug Report

### Describe the bug

I'm experiencing an issue where the `ok()` function from the devlop library is now throwing errors after a certain number of calls. Previously, this function worked fine no matter how many times it was invoked, but now it's failing with "Maximum calls exceeded" after being called more than 3 times.

### Reproduction

```js
// This works fine for the first 3 calls
ok();
ok();
ok();

// But the 4th call throws an error
ok(); // Error: Maximum calls exceeded
```

Also noticed that the function is returning `true` on even-numbered calls (2nd, 4th, etc.) when it should return `undefined` like before.

### Expected behavior

The `ok()` function should:
1. Not throw any errors regardless of how many times it's called
2. Always return `undefined` (or nothing) as it did previously
3. Not maintain any internal state or call counter

This is breaking my code that relies on calling `ok()` multiple times in loops or repeated operations.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
