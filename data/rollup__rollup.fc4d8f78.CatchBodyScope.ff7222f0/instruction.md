# Bug Report

### Describe the bug

I'm encountering an issue with variable redeclaration handling in catch blocks. When declaring a `var` with the same name as the catch parameter, the behavior seems incorrect - the variable is not being properly shadowed by the catch parameter as it should be.

### Reproduction

```js
try {
  throw new Error('test');
} catch (e) {
  var e = 'redeclared';
  console.log(e); // Should print 'redeclared'
}
```

In this case, the `var e` declaration inside the catch block should be hoisted but the assignment should go to the catch parameter `e`. However, the current behavior doesn't seem to handle this correctly.

Another related case:

```js
try {
  throw new Error('test');
} catch (error) {
  var error;
  var error = 'something';
  // Multiple var declarations with same name as catch parameter
}
```

### Expected behavior

According to JavaScript semantics, when you declare a `var` with the same name as a catch clause parameter:
- The `var` declaration should be hoisted to the function scope
- But the assignment should go to the catch parameter (which shadows it locally)
- The catch parameter should take precedence within the catch block

This is standard JavaScript scoping behavior for catch blocks.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
