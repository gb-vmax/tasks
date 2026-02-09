# Bug Report

### Describe the bug

I'm encountering an issue with variable redeclaration checking in function scopes. It seems like the logic for determining when redeclarations should be allowed is not working correctly.

### Reproduction

```js
function test() {
  let x = 1;
  var x = 2; // This should throw a redeclaration error but doesn't
}
```

According to JavaScript semantics, `let` and `var` should not be allowed to redeclare each other in the same scope. However, the current behavior is allowing this redeclaration when it shouldn't.

The issue appears to be related to how function-scoped (`var`, `function`) and block-scoped (`let`, `const`) declarations interact with each other during the declaration phase.

### Expected behavior

When trying to redeclare a `let`/`const` variable with `var` or vice versa in the same function scope, a redeclaration error should be thrown. The only valid redeclarations should be:
- `var` with `var`
- `function` with `function`
- `var` with `function` (and vice versa)
- `var`/`function` with function parameters

### Additional context

This seems to have broken recently and is causing incorrect compilation behavior where code that should fail is being accepted.

---
Repository: /testbed
