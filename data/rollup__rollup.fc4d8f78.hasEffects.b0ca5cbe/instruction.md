# Bug Report

### Describe the bug

I'm experiencing an issue where class methods are not being properly evaluated for side effects during tree-shaking. It seems like the bundler is incorrectly removing method definitions that should be kept because they have side effects.

### Reproduction

```js
class MyClass {
  method() {
    console.log('This has side effects');
    globalState.value = 42;
  }
}

// The method gets tree-shaken even though it has side effects
const instance = new MyClass();
```

When bundling this code, the method definition is being removed even though calling it would produce side effects. The method body contains statements that modify global state and produce console output, but the bundler treats it as if it's pure and can be safely removed.

### Expected behavior

Methods with side effects should be preserved during tree-shaking. The bundler should analyze the method body and detect that it has side effects (console.log, global state modification, etc.) and keep the method definition in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
