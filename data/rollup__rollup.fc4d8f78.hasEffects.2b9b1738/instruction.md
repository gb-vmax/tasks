# Bug Report

### Describe the bug

I'm experiencing an issue with class declarations that have side effects. When a class has a superclass or decorators that produce side effects, the bundler is not correctly detecting these effects in certain scenarios.

### Reproduction

```js
class Base {
  constructor() {
    console.log('Base constructor called');
  }
}

class Derived extends Base {
  constructor() {
    super();
  }
}

// The side effect from the Base class should be detected
new Derived();
```

Also happens with decorated classes:

```js
function myDecorator(target) {
  console.log('Decorator applied');
  return target;
}

@myDecorator
class MyClass {
  // ...
}
```

### Expected behavior

The bundler should properly detect and preserve side effects from:
- Superclass constructors and initialization
- Class decorators
- Class body initialization

These side effects should not be incorrectly tree-shaken or optimized away.

### Additional context

This seems to affect how the bundler determines whether a class declaration has side effects. In some cases, classes with clear side effects are being treated as if they have no effects, leading to incorrect optimization.

---
Repository: /testbed
