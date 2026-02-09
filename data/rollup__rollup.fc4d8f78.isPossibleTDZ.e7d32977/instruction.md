# Bug Report

### Describe the bug

I'm experiencing an issue with temporal dead zone (TDZ) detection in rollup. Variables that should be accessible are incorrectly being flagged as TDZ violations, causing the bundler to behave unexpectedly.

### Reproduction

```js
// This code should work fine but rollup treats it as a TDZ error
function test() {
  const x = 1;
  return x;
}
```

The variable `x` is declared before use, but it's being treated as if it's accessed before initialization. This seems to happen with variables that aren't actually in the temporal dead zone.

### Expected behavior

Variables declared with `const` or `let` should only be flagged as TDZ violations when they are actually accessed before their declaration point. In the example above, `x` is clearly declared before being returned, so this should not be treated as a TDZ issue.

### System Info
- rollup version: latest
- Node version: 18.x

This is causing problems with valid code being incorrectly analyzed during the tree-shaking process. Any help would be appreciated!

---
Repository: /testbed
