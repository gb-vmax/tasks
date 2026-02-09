# Bug Report

### Describe the bug

I'm experiencing an issue where `new` expressions are being incorrectly tree-shaken from the bundle even when they have side effects. Specifically, constructor calls that should be retained are being removed during the build process.

### Reproduction

```js
class MyClass {
  constructor() {
    console.log('Side effect!');
    window.someGlobal = true;
  }
}

// This constructor call gets removed even though it has side effects
new MyClass();
```

The `new MyClass()` statement is being eliminated from the output bundle, but it shouldn't be since the constructor modifies global state.

### Expected behavior

Constructor invocations with side effects should be preserved in the bundle. The `new MyClass()` call should appear in the output since it has observable side effects (logging and setting a global variable).

### Additional context

This seems to affect standalone `new` expressions where the result isn't assigned to a variable. The tree-shaking logic appears to be too aggressive in determining whether these expressions can be safely removed.

---
Repository: /testbed
