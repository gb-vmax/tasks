# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations inside catch blocks. When declaring a `var` with the same name as the catch parameter, the behavior seems incorrect - the variable is not being properly hoisted and the initialization is not handled as expected.

### Reproduction

```js
try {
  throw new Error('test');
} catch (e) {
  var e = 'redeclared';
  console.log(e); // Should print 'redeclared'
}
console.log(e); // Should be accessible due to var hoisting
```

According to JavaScript semantics, when you declare a `var` with the same name as a catch parameter, the `var` should be hoisted to the function scope but the assignment should go to the catch parameter. However, it seems like the initialization is not being properly linked.

### Expected behavior

The `var` declaration should be hoisted to the parent scope while the assignment updates the catch parameter locally. The initialization should be preserved when hoisting the variable declaration.

### Additional context

This affects code that relies on the specific scoping rules of catch blocks combined with var hoisting. The issue appears to be related to how catch body scopes handle variable declarations that conflict with catch parameters.

---
Repository: /testbed
