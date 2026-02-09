# Bug Report

### Describe the bug

When calling methods on number literals (like `toFixed()`, `toString()`, etc.), the return type analysis is broken and doesn't correctly identify the return type of these method calls.

### Reproduction

```js
const num = 42;
const result = num.toFixed(2);
// The return type should be recognized as a string, but it's not being detected correctly
```

Another example:
```js
const value = 3.14159;
const str = value.toString();
// Similar issue - the method call on the number literal isn't being analyzed properly
```

### Expected behavior

Number literal methods should be properly recognized and their return types should be correctly inferred. Methods like `toFixed()`, `toString()`, `toExponential()`, etc. should have their return expressions properly tracked.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started recently - the type analysis for number method calls used to work correctly but now fails to properly track the return expressions.

---
Repository: /testbed
