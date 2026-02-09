# Bug Report

### Describe the bug

I'm encountering an issue with `var` declarations inside `catch` blocks. When a `var` variable has the same name as the catch parameter, the behavior seems incorrect - the variable is being hoisted but the local shadowing by the catch parameter isn't working as expected.

### Reproduction

```js
try {
  throw new Error('test');
} catch (err) {
  var err = 'reassigned';
  console.log(err); // Should print 'reassigned'
}
console.log(err); // err should be hoisted but undefined
```

In this case, the `var err` declaration should be hoisted to the outer scope, but within the catch block, the assignment should go to the catch parameter `err`, not create a new variable.

### Expected behavior

According to JavaScript semantics:
- The `var err` should be hoisted to the function/global scope
- Inside the catch block, `err` should refer to the catch parameter
- Assignments to `err` inside the catch should modify the parameter, not the hoisted var

### Additional context

This appears to be related to how variable declarations are being resolved in catch block scopes. The scoping rules for `var` declarations that share names with catch parameters seem to have changed.

---
Repository: /testbed
