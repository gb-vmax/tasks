# Bug Report

### Describe the bug

I'm experiencing an issue where decorators are being incorrectly tree-shaken from my code. After bundling, decorators that should be included in the output are being removed, causing runtime errors when the decorated code tries to execute.

### Reproduction

```js
function log(target, key, descriptor) {
  const original = descriptor.value;
  descriptor.value = function(...args) {
    console.log(`Calling ${key}`);
    return original.apply(this, args);
  };
  return descriptor;
}

class MyClass {
  @log
  myMethod() {
    return 'hello';
  }
}

const instance = new MyClass();
instance.myMethod(); // Expected to log "Calling myMethod" but decorator is missing
```

When I bundle this code, the `@log` decorator gets removed entirely. The bundled output doesn't include the decorator logic, so the logging behavior is lost.

### Expected behavior

Decorators should be preserved in the bundled output since they have side effects (modifying the descriptor). The decorator function should be called at runtime and the method should be wrapped as expected.

### Additional context

This seems to have started happening recently. I'm not sure if this is related to changes in how side effects are detected for decorators, but it's breaking my builds. The decorators are being treated as pure code that can be safely removed, even though they clearly have side effects.

---
Repository: /testbed
