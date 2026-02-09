# Bug Report

### Describe the bug

I'm encountering an issue where variables declared with `let` or `const` in certain scopes are not being properly detected as potentially causing Temporal Dead Zone (TDZ) errors. The bundler appears to be incorrectly optimizing away code that should be preserved due to possible TDZ violations.

### Reproduction

```js
// module.js
export function test() {
  console.log(x); // Should cause TDZ error
  let x = 5;
}

// main.js
import { test } from './module.js';
test();
```

When bundling this code, the `console.log(x)` statement gets incorrectly tree-shaken or optimized in a way that suggests the bundler doesn't recognize the TDZ issue with the `let` declaration.

### Expected behavior

The bundler should recognize that accessing `x` before its declaration is a potential TDZ error and preserve the code accordingly. Variables declared with `let` and `const` should be treated differently from `var` declarations when checking for side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
