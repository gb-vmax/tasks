# Bug Report

### Describe the bug

When using tagged template expressions with multiple template expressions, the last expression in the template is not being evaluated for side effects. This causes issues where side effects from the final expression are incorrectly ignored during tree-shaking or bundling.

### Reproduction

```js
function tag(strings, ...values) {
  return strings[0] + values.join('');
}

let sideEffect = 0;

function increment() {
  sideEffect++;
  return sideEffect;
}

// The last increment() call's side effect should be detected
const result = tag`value1: ${increment()} value2: ${increment()}`;
```

In this case, both `increment()` calls should be recognized as having side effects, but the second (last) one is being skipped during the side effect analysis.

### Expected behavior

All expressions within a tagged template literal should be checked for side effects, including the last one. The bundler should not incorrectly tree-shake code that has observable side effects in any position of the template expression list.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
