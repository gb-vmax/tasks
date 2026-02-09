# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations when they reference each other. It seems like the order of initialization has changed and now declarations that depend on previously declared variables in the same statement are not being handled correctly.

### Reproduction

```js
const { a, b = a } = { a: 1 };
console.log(b); // Should output 1
```

Or with destructuring:

```js
const [x, y = x] = [5];
console.log(y); // Should output 5
```

### Expected behavior

When a variable declarator uses a default value that references another variable from the same declaration statement, it should be able to access that variable. The variable `b` (or `y`) should resolve to the value of `a` (or `x`) from the same destructuring assignment.

### Additional context

This appears to be related to how variable declarations are being initialized. The declarations need to be processed in the correct order so that earlier variables are available when later ones are initialized with default values that reference them.

---
Repository: /testbed
