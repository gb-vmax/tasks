# Bug Report

### Describe the bug

When using markdown emphasis with custom options, I'm getting an error that doesn't make sense. The error message says it's expecting `*` or `_`, but it's rejecting valid markers.

### Reproduction

```js
const state = {
  options: {
    emphasis: '*'
  }
};

// This throws an error even though '*' should be valid
checkEmphasis(state);
```

The error message says:
```
Cannot serialize emphasis with `*` for `options.emphasis`, expected `*`, or `_`
```

This is confusing because I'm using `*` which is supposedly one of the expected values, but it's still throwing an error.

### Expected behavior

Using either `*` or `_` as the emphasis marker should work without throwing an error. The validation should only fail if I use something other than these two characters.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
