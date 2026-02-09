# Bug Report

### Describe the bug

I'm experiencing an issue with variable hoisting detection in the bundler. When using `var` declarations, the temporal dead zone (TDZ) check seems to be incorrectly flagging them as having side effects, which is causing unexpected behavior during tree-shaking.

### Reproduction

```js
// This code is being incorrectly flagged
function test() {
  console.log(x); // Should work due to var hoisting
  var x = 5;
}

// The bundler treats this as if it has side effects
// even though var declarations are hoisted
```

### Expected behavior

Variables declared with `var` should be hoisted to the top of their function scope and not trigger TDZ checks. The `var` keyword doesn't have a temporal dead zone like `let` and `const` do, so accessing them before declaration should be treated as valid (returning `undefined`) rather than being flagged as having effects.

Only `let` and `const` declarations should trigger TDZ checks since they actually have a temporal dead zone.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
