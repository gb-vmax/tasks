# Bug Report

### Describe the bug

When accessing the AST property on a module that's already been cached in the LRU cache, the property returns `undefined` instead of the cached AST. This causes issues when the same module's AST is requested multiple times during the build process.

### Reproduction

```js
// First access - works fine
const ast1 = moduleInfo.ast;
console.log(ast1); // Outputs the AST object

// Module gets added to LRU cache
// Second access - returns undefined
const ast2 = moduleInfo.ast;
console.log(ast2); // undefined (expected: AST object)
```

### Expected behavior

The AST should be returned correctly on subsequent accesses when it's already in the LRU cache. Both `ast1` and `ast2` should reference the same AST object.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
