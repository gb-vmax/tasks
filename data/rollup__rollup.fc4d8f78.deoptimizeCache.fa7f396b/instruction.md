# Bug Report

### Describe the bug

I'm experiencing an issue with class-based code where deoptimization doesn't seem to be happening correctly. After some recent changes, the tree-shaking behavior appears to have regressed - code that should be marked as having side effects is being incorrectly removed during optimization.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
  
  doSomething() {
    // This should trigger deoptimization
    this.value = Math.random();
  }
}

const instance = new MyClass();
instance.doSomething();
```

When bundling the above code, methods and properties that should be preserved are being tree-shaken away, even though they have side effects. The deoptimization cache doesn't appear to be invalidating properly.

### Expected behavior

The deoptimization mechanism should properly mark all properties as potentially having side effects, preventing incorrect removal during the optimization phase. Class methods and properties should be preserved when they can have observable effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
