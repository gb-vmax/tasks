# Bug Report

### Describe the bug

I'm experiencing an issue with method decorators where methods with decorators are being incorrectly tree-shaken even when they have side effects. It seems like the bundler is not properly detecting that decorated methods should be retained.

### Reproduction

```js
class MyClass {
  @decorator
  myMethod() {
    console.log('This has side effects');
    doSomething();
  }
}

const instance = new MyClass();
```

When bundling this code, the method gets removed from the output even though:
1. The decorator itself might have side effects
2. The method body contains side effects (console.log, function calls)

### Expected behavior

Methods with decorators should be preserved in the bundle if either the decorator or the method body has side effects. The current behavior is removing methods that should be kept, breaking the application at runtime.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
