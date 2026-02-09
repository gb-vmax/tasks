# Bug Report

### Describe the bug

When using conditional expressions (ternary operators) with tree-shaking, the bundler is incorrectly removing code when the consequent branch is optimized out. The alternate branch gets mangled with leftover syntax characters from the removed parts.

### Reproduction

```js
// input.js
const result = condition ? removedBranch() : keptBranch();
export { result };
```

When `condition` is statically determined to be false and `removedBranch()` is tree-shaken away, the output contains invalid syntax with remnants of the `?` or `:` operators not being properly cleaned up.

Example output:
```js
const result = : keptBranch();
```

Or in some cases:
```js
const result = ? keptBranch();
```

### Expected behavior

When a branch of a ternary expression is removed during tree-shaking, the output should be clean JavaScript with just the used branch:
```js
const result = keptBranch();
```

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to affect cases where the conditional test can be statically evaluated and one of the branches is eliminated during dead code removal.

---
Repository: /testbed
