# Bug Report

### Describe the bug

I'm encountering an issue with tree-shaking where code that should be included in the bundle is being excluded, and conversely, code that should be excluded is being included. This seems to affect block statements and how they determine which child nodes should be included.

### Reproduction

```js
// example.js
function test() {
  const used = 1;
  const unused = 2;
  return used;
}

export { test };
```

When bundling this code, nodes that should be included based on `shouldBeIncluded()` are getting excluded, while nodes that shouldn't be included are being added to the bundle.

### Expected behavior

The bundler should correctly determine which statements within a block need to be included based on whether they're actually used. Statements that are referenced should be included, and unused statements should be tree-shaken away.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
