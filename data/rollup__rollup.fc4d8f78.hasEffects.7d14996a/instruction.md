# Bug Report

### Describe the bug

When using class declarations with decorators, the side effects are not being evaluated in the correct order. This causes issues where class decorators that should be checked for side effects are being skipped when the class identifier has already been marked as having effects.

### Reproduction

```js
// Class with decorators where the identifier marking happens too early
@decorator
class MyClass {
  constructor() {
    // ...
  }
}

// The decorator effects should be checked before returning,
// but the current implementation may return early and skip decorator checks
```

### Expected behavior

All side effects should be properly evaluated in the correct order:
1. Check superclass effects
2. Check class body effects  
3. Check parent node effects
4. Check decorator effects

The decorator effects should always be evaluated and not skipped due to early returns from other effect checks.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
