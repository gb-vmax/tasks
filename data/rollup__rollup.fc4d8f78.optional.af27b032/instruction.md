# Bug Report

### Describe the bug

I'm encountering an issue with optional chaining where the behavior seems inverted. When I use optional chaining (`?.`) in my code, it's being treated as if it's NOT optional, and when I don't use optional chaining, it's being treated as if it IS optional.

### Reproduction

```js
const obj = { a: { b: 1 } };

// This should safely access nested property
const result1 = obj?.a?.b;
// Expected: 1
// Actual: Throws/behaves as if optional is false

// This should throw/error on null
const obj2 = null;
const result2 = obj2.a.b;
// Expected: Error
// Actual: Behaves as if optional chaining is applied
```

The optional chaining operator seems to be doing the opposite of what it should - treating optional accesses as required and required accesses as optional.

### Expected behavior

Optional chaining (`?.`) should:
- Return `undefined` when accessing properties on `null`/`undefined`
- Not throw errors for missing nested properties

Regular property access (`.`) should:
- Throw errors when accessing properties on `null`/`undefined`
- Behave as normal member access

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
