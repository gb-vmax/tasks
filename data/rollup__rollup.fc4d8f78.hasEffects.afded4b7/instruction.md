# Bug Report

### Describe the bug

Decorators with side effects are being incorrectly tree-shaken from the output bundle. When a decorator expression has side effects (like logging, modifying global state, or performing I/O), these effects should be preserved in the final output, but they're being removed during the bundling process.

### Reproduction

```js
let counter = 0;

function track(target, propertyKey, descriptor) {
  counter++;
  console.log('Decorator applied');
  return descriptor;
}

class MyClass {
  @track
  myMethod() {
    return 'hello';
  }
}

// Expected: counter should be 1 and 'Decorator applied' should be logged
// Actual: decorator is removed from bundle, counter remains 0
```

### Expected behavior

Decorators that have side effects should be included in the bundle and executed. The decorator function should be called even if the decorated method/property is not directly referenced elsewhere in the code.

### Additional context

This appears to affect decorators that:
- Call external functions with side effects
- Modify global variables
- Perform logging or other observable operations

The bundler seems to be treating these decorators as pure and removing them during tree-shaking, even though they clearly have effects that should be preserved.

---
Repository: /testbed
