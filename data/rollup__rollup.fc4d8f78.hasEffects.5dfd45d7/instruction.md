# Bug Report

### Describe the bug

I'm encountering an issue with class declarations that have superclasses. It seems like the side effects from superclass expressions are not being properly evaluated in some cases, leading to incorrect tree-shaking behavior.

### Reproduction

```js
class Base {
  constructor() {
    console.log('Base constructor called');
  }
}

let sideEffect = false;

class Extended extends (sideEffect = true, Base) {
  method() {
    return 'test';
  }
}

// The superclass expression should always be evaluated
// but it appears to be incorrectly optimized away in some scenarios
```

When bundling code with class inheritance where the superclass is an expression with side effects, those side effects may not execute as expected. This can lead to runtime behavior that differs from what the source code suggests.

### Expected behavior

The superclass expression should always be evaluated, regardless of whether the class body or other parts have effects. Side effects in the superclass expression should not be optimized away during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
