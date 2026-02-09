# Bug Report

### Describe the bug

I'm experiencing an issue where side effects in conditional expressions (ternary operators) are not being detected correctly. It seems like the tree-shaking is being too aggressive and removing code that actually has side effects.

### Reproduction

```js
// This code should be preserved because of side effects
const result = condition ? sideEffect1() : sideEffect2();

// But it's getting removed during the build process
```

More specifically, when I have a ternary expression where both branches have side effects (like function calls that modify global state), the bundler is incorrectly treating it as if it has no effects and removing it from the output.

### Expected behavior

Code with side effects in conditional expressions should be preserved in the bundle, even if the return value isn't used. Both branches of a ternary operator should be checked for side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
