# Bug Report

### Describe the bug

I'm experiencing an issue where `new` expressions are being incorrectly tree-shaken when their properties are accessed. The bundler is removing constructor calls that should be retained because they have side effects through property access.

### Reproduction

```js
class MyClass {
  constructor() {
    console.log('Constructor called');
  }
  
  get myProperty() {
    console.log('Property accessed');
    return 'value';
  }
}

// This should be retained but gets removed
const value = new MyClass().myProperty;
```

When bundling this code, the `new MyClass()` expression gets tree-shaken out even though accessing `.myProperty` has observable side effects (the console logs). The constructor should be called and the property getter should execute, but instead the entire expression is removed from the output.

### Expected behavior

The `new` expression should be retained in the bundle when its properties are accessed, as the property access could have side effects. Both console logs should appear in the final output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
