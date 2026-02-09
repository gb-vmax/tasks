# Bug Report

### Describe the bug

I'm encountering an issue where variable references at the exact same position as their declaration are incorrectly flagged as Temporal Dead Zone (TDZ) violations. This seems to affect edge cases where the identifier start position equals the declaration start position.

### Reproduction

```js
// Example scenario that triggers the issue
const x = x; // self-referencing at same position
```

Or in a bundler context where source positions might align:

```js
let { value } = { value: someComputation() };
// When the identifier 'value' on the left has the same start position
// as the declaration, it's incorrectly treated as a TDZ access
```

### Expected behavior

Variables should only be considered as TDZ violations when they are accessed **before** their declaration (start position strictly less than declaration position), not at the exact same position. The current behavior is too strict and flags valid code as problematic.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to be related to how the TDZ checking logic compares positions. The comparison should probably be strict inequality rather than less-than-or-equal.

---
Repository: /testbed
