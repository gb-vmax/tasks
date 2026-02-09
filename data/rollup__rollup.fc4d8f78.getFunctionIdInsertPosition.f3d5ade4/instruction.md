# Bug Report

### Describe the bug

When exporting a default function declaration, the generated code has incorrect spacing/positioning. The function name insertion point seems to be calculated incorrectly, resulting in malformed output.

### Reproduction

```js
// Input code
export default function() {
  return 'test';
}

// After processing, the function identifier gets inserted at the wrong position
// Expected: export default function _default() { ... }
// Actual: The identifier appears in an unexpected location
```

This also affects generator functions:

```js
export default function*() {
  yield 1;
}
```

### Expected behavior

When a default export is an anonymous function (regular or generator), the bundler should correctly insert a default identifier at the appropriate position - right after the `function` keyword (or after the `*` for generator functions).

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
