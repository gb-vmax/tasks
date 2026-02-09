# Bug Report

### Describe the bug

I'm encountering an issue with optional chaining when accessing properties on objects that could be `undefined`. The behavior seems incorrect when the object evaluates to `undefined` specifically.

### Reproduction

```js
const obj = undefined;
const result = obj?.property;
```

When using optional chaining on an `undefined` value, the code doesn't behave as expected. It seems like there's a problem with how `undefined` values are being handled in the optional chaining logic.

### Expected behavior

Optional chaining should properly short-circuit when the object is `undefined`, preventing any further property access and returning `undefined` without side effects.

### Additional context

This appears to be related to how member expressions with optional chaining handle `undefined` values. The issue might be specific to cases where the base object is `undefined` rather than `null`.

---
Repository: /testbed
