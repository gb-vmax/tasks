# Bug Report

### Describe the bug

I'm encountering an issue where property access tracking seems to be broken in certain scenarios. When accessing properties on local variables, the code is incorrectly determining that side effects exist even when they shouldn't.

### Reproduction

```js
const obj = {
  prop: {
    nested: 'value'
  }
};

// Accessing obj.prop.nested
// Expected: Should not report side effects if the variable hasn't been reassigned
// Actual: Reports side effects incorrectly
```

The problem appears to be related to how accessed properties are being tracked. It seems like the logic for determining whether an interaction has effects is not working as expected - specifically when checking if a path has already been tracked.

### Expected behavior

Property accesses on local variables that haven't been reassigned should correctly report whether they have side effects. The tracking mechanism should properly identify when a path has already been visited to avoid redundant checks.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
