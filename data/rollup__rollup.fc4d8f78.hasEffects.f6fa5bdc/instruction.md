# Bug Report

### Describe the bug

I'm experiencing an issue with method decorators where the bundler seems to be incorrectly evaluating side effects. Methods with decorators are being tree-shaken even when the decorators have side effects that should be preserved.

### Reproduction

```js
function sideEffect(target, key, descriptor) {
  console.log('Decorator applied');
  return descriptor;
}

class MyClass {
  @sideEffect
  myMethod() {
    console.log('Method called');
  }
}

// The decorator side effect is not preserved during bundling
```

When bundling this code, the decorator's side effect (`console.log('Decorator applied')`) is being removed even though it should be executed. The bundler appears to be treating the decorated method as having no effects when it actually does.

### Expected behavior

Methods with decorators that have side effects should be preserved during tree-shaking. The decorator function should be called and its side effects should be maintained in the output bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
