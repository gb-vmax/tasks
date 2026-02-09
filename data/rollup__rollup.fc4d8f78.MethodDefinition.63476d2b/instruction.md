# Bug Report

### Describe the bug

I'm experiencing an issue with method decorators where methods with decorators that have side effects are being incorrectly tree-shaken from the bundle. The methods are removed even though their decorators should cause them to be retained.

### Reproduction

```js
function sideEffectDecorator(target, propertyKey, descriptor) {
  console.log('Decorator applied');
  // Some side effect logic
}

class MyClass {
  @sideEffectDecorator
  myMethod() {
    return 'hello';
  }
}
```

When bundling this code, the `myMethod` is being removed from the output even though the decorator has side effects that should prevent tree-shaking.

### Expected behavior

Methods with decorators that have side effects should be preserved in the bundle. The decorator's side effects should be evaluated to determine if the method can be safely removed during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
