# Bug Report

### Describe the bug

When declaring a variable with a named class expression, the variable name is incorrectly being forbidden for other variables in the class scope. This causes naming conflicts where there shouldn't be any.

### Reproduction

```js
const MyClass = class NamedClass {
  method() {
    // MyClass should be accessible here
    return MyClass;
  }
}
```

In this case, the bundler is incorrectly applying name restrictions. The variable `MyClass` gets its name forbidden when it shouldn't be, leading to unexpected mangling or errors during the build process.

### Expected behavior

The variable name should only be forbidden for variables that are NOT the same as the declared variable itself. When a class expression has its own name (like `NamedClass` in the example), the outer variable name (`MyClass`) should still be usable within the class scope without conflicts.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
