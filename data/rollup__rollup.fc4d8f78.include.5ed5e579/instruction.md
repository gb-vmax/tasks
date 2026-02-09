# Bug Report

### Describe the bug

When using `new` expressions in the code, the tree-shaking behavior seems broken. Classes/constructors that should be included in the bundle are being removed, causing runtime errors when the code tries to instantiate objects.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
  
  getValue() {
    return this.value;
  }
}

// This instantiation gets removed during bundling
const instance = new MyClass();
console.log(instance.getValue());
```

After bundling, the output is missing the necessary code and throws an error at runtime because `MyClass` was incorrectly tree-shaken away.

### Expected behavior

The bundler should recognize that `new MyClass()` requires the class definition to be included in the output bundle. The code should execute without errors after bundling.

### Additional context

This seems to have started happening recently. The same code was working fine before. It's particularly problematic when the constructor or class methods have side effects that are necessary for the application to function correctly.

---
Repository: /testbed
