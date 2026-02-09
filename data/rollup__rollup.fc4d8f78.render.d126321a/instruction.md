# Bug Report

### Describe the bug

I'm encountering an issue with `throw` statement rendering in the bundled output. When a `throw` statement is used without a space between the keyword and the argument (e.g., `throw(error)`), the output is malformed with the space inserted at the wrong position.

### Reproduction

```js
// Input code
function test() {
  throw(new Error('test'));
}

// After bundling, the output has incorrect spacing
// Expected: throw (new Error('test'));
// Actual: thro w(new Error('test'));
```

The space is being inserted at the wrong character offset, resulting in invalid JavaScript syntax in the bundled output.

### Expected behavior

The bundler should correctly insert a space between `throw` and the argument when needed, producing valid JavaScript like `throw (new Error('test'))` instead of breaking the `throw` keyword itself.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
