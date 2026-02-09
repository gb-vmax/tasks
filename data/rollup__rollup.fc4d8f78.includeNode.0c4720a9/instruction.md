# Bug Report

### Describe the bug

When bundling code with class expressions assigned to variables, I'm seeing incorrect variable name conflicts being generated. It looks like variables that should be allowed to use the same name are being forbidden from doing so.

### Reproduction

```js
// Input code
const MyClass = class {
  method() {
    // Reference to MyClass from within the class
    return MyClass;
  }
};
```

When this gets bundled, the variable name `MyClass` is incorrectly being marked as forbidden for the class's internal reference to itself. This causes the bundler to rename variables that shouldn't need renaming.

### Expected behavior

The class expression should be able to reference its assigned variable name (`MyClass`) from within its own scope without triggering name conflicts. The bundler should only forbid the name for *other* variables that are accessed from outside, not for the variable the class is assigned to.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
