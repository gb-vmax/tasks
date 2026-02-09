# Bug Report

### Describe the bug

When using `super` in class methods, I'm getting runtime errors about `that` being undefined. The code was working fine before, but now any class that extends another class and uses `super` throws an error.

### Reproduction

```js
class Parent {
  constructor() {
    this.value = 'parent';
  }
  
  getValue() {
    return this.value;
  }
}

class Child extends Parent {
  constructor() {
    super();
    this.value = 'child';
  }
  
  getParentValue() {
    return super.getValue();
  }
}

const instance = new Child();
console.log(instance.getParentValue()); // Error: 'that' is not defined
```

### Expected behavior

The `super` keyword should correctly reference the parent class methods and properties. The code above should print `'child'` without any errors.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
