# Bug Report

### Describe the bug

I'm encountering an issue with switch statements when all cases are removed during tree-shaking. The discriminant expression is still being rendered even when the entire switch body is empty.

### Reproduction

```js
// input.js
const value = getSomeValue();

switch (value) {
  case 'unused':
    unusedFunction();
    break;
}
```

When all cases are removed due to dead code elimination (e.g., when `unusedFunction` is never imported/used), the switch statement should be completely removed. However, the discriminant expression (`getSomeValue()`) is still being rendered in the output, which can cause side effects or unnecessary code execution.

### Expected behavior

When all cases in a switch statement are tree-shaken away, the entire switch statement including the discriminant should be removed from the output. The discriminant should only be rendered if there are actually cases to evaluate.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
