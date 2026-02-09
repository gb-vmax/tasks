# Bug Report

### Describe the bug

When accessing variables in nested scopes, the variable lookup order appears to be incorrect. Variables defined in the current scope are not being found before checking parent scopes, which can lead to the wrong variable being resolved when there are shadowing variables with the same name.

### Reproduction

```js
// Outer scope
let x = 'outer';

function test() {
  // Inner scope - this should shadow the outer x
  let x = 'inner';
  
  // This should reference the inner x, but may incorrectly resolve to outer x
  console.log(x);
}
```

In the above example, the inner `x` should be resolved first since it's in the current scope, but the variable lookup might be checking outside variables before checking the current scope's own variables.

### Expected behavior

Variable resolution should follow the standard scoping rules:
1. Check if the variable exists in the current scope first
2. Only look in parent scopes if not found in current scope

This ensures that variable shadowing works correctly and inner scope variables take precedence over outer ones with the same name.

### Additional context

This seems to affect how `findVariable` determines which variable to return when the same name exists in multiple nested scopes. The lookup priority appears to have changed recently.

---
Repository: /testbed
