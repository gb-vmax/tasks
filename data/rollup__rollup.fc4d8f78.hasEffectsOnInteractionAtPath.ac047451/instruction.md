# Bug Report

### Describe the bug

I'm encountering an issue where accessing literal number properties is not being treated correctly in terms of side effects detection. When I access a literal number value directly (without any property access), the bundler seems to be incorrectly assuming it has side effects.

### Reproduction

```js
const x = 42;
console.log(x); // This should be considered side-effect free for the literal itself
```

The issue appears when the bundler analyzes expressions involving literal numbers. Direct access to a literal number value is being flagged as having effects when it shouldn't be.

### Expected behavior

Accessing a literal number value directly (path length of 0) should not be considered as having side effects. Only accessing properties on the number (like calling methods such as `.toFixed()`) should potentially have effects.

For example:
- `42` - no effects (path length 0)
- `(42).toFixed()` - may have effects (path length 1+)

### Additional context

This seems to affect how the bundler optimizes code that uses numeric literals. The overly conservative side effect detection may be preventing proper tree-shaking or dead code elimination in some cases.

---
Repository: /testbed
