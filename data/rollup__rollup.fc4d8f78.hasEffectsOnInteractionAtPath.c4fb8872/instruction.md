# Bug Report

### Describe the bug

I'm encountering an issue where classes are being incorrectly treated as having side effects when they're used without the `new` keyword. The bundler is including classes in the output even when they should be tree-shaken because they're called as regular functions (which would throw an error at runtime anyway).

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
}

// This should be tree-shaken since calling a class without 'new' throws an error
// But it's being kept in the bundle
MyClass();

export default {};
```

The class `MyClass` is being retained in the final bundle even though:
1. It's called without `new` (which would throw a TypeError at runtime)
2. The result is not used anywhere
3. It should be safe to remove during tree-shaking

### Expected behavior

Classes that are called as regular functions (without `new`) should be tree-shaken if their result is unused, since calling a class without `new` always throws an error and cannot have meaningful side effects.

### Additional context

This seems to affect dead code elimination. The bundler appears to be treating class calls (without `new`) as if they might have side effects, when in reality they just throw errors.

---
Repository: /testbed
