# Bug Report

### Describe the bug

When bundling code that contains `new` expressions (constructor calls), the output is malformed. The constructor arguments appear to be duplicated in the generated code, and the actual constructor/class name is missing entirely from the output.

### Reproduction

```js
// Input code
class MyClass {
  constructor(a, b) {
    this.a = a;
    this.b = b;
  }
}

const instance = new MyClass(1, 2);
```

After bundling, the output for the `new MyClass(1, 2)` expression is broken - the arguments are rendered twice and `MyClass` itself doesn't appear in the output.

### Expected behavior

The `new` expression should be rendered correctly in the bundled output with the constructor name followed by the arguments once, like `new MyClass(1, 2)`.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
