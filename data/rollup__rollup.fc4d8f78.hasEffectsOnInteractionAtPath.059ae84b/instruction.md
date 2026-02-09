# Bug Report

### Describe the bug

When calling methods on a class instance, the side effects detection appears to be incorrect. Specifically, method calls on class instances are not being properly tracked for side effects, which can lead to incorrect tree-shaking behavior.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 0;
  }
  
  increment() {
    this.value++;
    console.log(this.value);
  }
}

const instance = new MyClass();
instance.increment(); // This call's side effects may not be detected correctly
```

The issue seems to occur when:
1. You have a class with methods that have side effects
2. You call those methods on an instance of the class
3. The bundler doesn't correctly identify that these method calls have side effects

### Expected behavior

Method calls on class instances should be properly analyzed for side effects. If a method has side effects (like modifying state or calling console.log), those effects should be detected and the code should not be incorrectly removed during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
