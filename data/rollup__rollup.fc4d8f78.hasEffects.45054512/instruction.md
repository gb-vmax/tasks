# Bug Report

### Describe the bug

When a class extends a superclass that has side effects, the order of operations seems to be causing incorrect behavior. The class body's effects are being evaluated in the wrong sequence relative to the superclass effects.

### Reproduction

```js
class Base {
  constructor() {
    console.log('Base constructor');
    sideEffect();
  }
}

class Derived extends Base {
  static {
    console.log('Static block');
  }
}
```

In this case, the side effects from the superclass and the class body are not being checked in the correct order, which can lead to incorrect tree-shaking decisions or missed side effects during bundling.

### Expected behavior

The superclass effects should be fully evaluated before moving on to check other effects. The current implementation appears to be checking effects in an inconsistent order, which could result in:
- Incorrect dead code elimination
- Missing side effects in the bundle
- Unexpected behavior when classes with side effects are tree-shaken

### System Info
- Rollup version: latest
- Node version: 18.x

This seems related to how the AST processes class declarations with inheritance. Any class that extends another class with side effects might be affected.

---
Repository: /testbed
