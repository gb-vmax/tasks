# Bug Report

### Describe the bug

I'm encountering an issue with `super` keyword handling in class inheritance scenarios. When using `super` in derived classes, the variable binding appears to be incorrect, causing unexpected behavior during bundling.

### Reproduction

```js
class Base {
  constructor() {
    this.value = 'base';
  }
  
  getValue() {
    return this.value;
  }
}

class Derived extends Base {
  constructor() {
    super();
    this.value = 'derived';
  }
  
  getValue() {
    return super.getValue();
  }
}

const instance = new Derived();
console.log(instance.getValue());
```

When bundling code that uses `super` in method calls or property access, the output doesn't work as expected. The `super` keyword seems to be resolved incorrectly.

### Expected behavior

The `super` keyword should properly reference the parent class methods and properties. The bundled code should maintain correct inheritance behavior.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to recent changes in how variables are resolved in the AST.

---
Repository: /testbed
