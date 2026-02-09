# Bug Report

### Describe the bug

I'm experiencing an issue where the `undefined` global variable is being treated incorrectly during tree-shaking. Code that accesses `undefined` is being removed even though it should be preserved, leading to unexpected behavior in the bundled output.

### Reproduction

```js
// Input code
const value = undefined;
console.log(value);

// After bundling, the code gets incorrectly removed
// Expected: code should be preserved
// Actual: code is tree-shaken away
```

Another example:
```js
function checkValue(x) {
  if (x === undefined) {
    return 'not defined';
  }
  return 'defined';
}

// The function body gets incorrectly optimized/removed
```

### Expected behavior

The bundler should recognize that accessing `undefined` is a safe operation with no side effects, but the code should still be preserved when it's actually used. The `undefined` global should be treated specially since it's a valid JavaScript global that can be safely accessed.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The bundler appears to be incorrectly flagging `undefined` access as having effects, which causes tree-shaking to behave unexpectedly.

---
Repository: /testbed
