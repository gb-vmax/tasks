# Bug Report

### Describe the bug

When declaring a variable with an anonymous class expression, the class name inference is not working properly. The class should inherit the variable name when it doesn't have an explicit name, but this seems to be broken.

### Reproduction

```js
const MyClass = class {
  static getName() {
    return this.name;
  }
};

console.log(MyClass.getName()); // Expected: 'MyClass', but not working correctly
```

The issue occurs when assigning an anonymous class expression to a variable. The class should automatically get the variable's name, but it appears this mechanism is failing.

### Expected behavior

Anonymous class expressions assigned to variables should inherit the variable name for their internal `name` property. This is standard JavaScript behavior that should be preserved during bundling.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
