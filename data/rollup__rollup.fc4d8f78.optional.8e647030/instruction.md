# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining in member expressions. When using the optional chaining operator (`?.`), the behavior seems to be inverted - it treats optional members as non-optional and vice versa.

### Reproduction

```js
// Case 1: Using optional chaining
const obj = { nested: { value: 42 } };
obj?.nested?.value  // Expected to work, but throws/behaves incorrectly

// Case 2: Without optional chaining
const result = obj.nested.value  // Expected to throw on null/undefined, but doesn't
```

The optional flag appears to be set incorrectly, causing the opposite behavior of what's expected.

### Expected behavior

- `obj?.property` should safely access the property and return undefined if obj is null/undefined
- `obj.property` should throw an error when obj is null/undefined
- The optional chaining operator should work as specified in the ECMAScript standard

### System Info

- Rollup version: latest main branch
- Node version: v18.x

This seems like a regression that affects optional chaining behavior throughout the codebase. Any member expression using `?.` is affected.

---
Repository: /testbed
