# Bug Report

### Describe the bug

I'm experiencing an issue with `this` binding in module scope. It seems like `this` is being incorrectly aliased to the module context when it shouldn't be, and vice versa.

### Reproduction

```js
// In a module context, this should be undefined
console.log(this); // Expected: undefined, but gets module context instead

// In a non-module context (like a function), this should use module context
function myFunction() {
  console.log(this); // Expected: module context, but gets null/undefined
}
```

The behavior appears to be inverted - when `this` is used at the module level, it's getting bound to the module context when it should be `undefined`. Conversely, when used in other scopes where it should reference the module context, it's returning `null` instead.

### Expected behavior

- `this` at module scope should be `undefined` and trigger the appropriate warning
- `this` in non-module lexical boundaries should correctly reference the module context

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like it might be a regression as the logic appears to be backwards. The condition for determining when to use module context seems inverted.

---
Repository: /testbed
