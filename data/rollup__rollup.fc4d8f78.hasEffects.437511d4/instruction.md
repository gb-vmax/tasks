# Bug Report

### Describe the bug

Tagged template expressions are not being properly evaluated for side effects. When using a tagged template literal, the bundler is incorrectly removing code that should be kept because it has side effects.

### Reproduction

```js
// This code should be kept but gets removed
function sideEffect() {
  console.log('side effect');
  return (strings, ...values) => strings[0];
}

sideEffect()`template`;

// The function call has side effects and should not be tree-shaken
```

### Expected behavior

Tagged template expressions should be retained when:
1. The tag function itself has side effects
2. The tag function call has side effects on interaction

The bundler should correctly detect these side effects and prevent the code from being removed during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
