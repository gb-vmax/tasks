# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in block scopes where `var` declarations are not being properly hoisted across parent scopes. When declaring a `var` inside a nested block, it seems like the variable is only registered in the immediate block scope instead of being accessible in parent scopes as expected with `var` hoisting behavior.

### Reproduction

```js
function test() {
  if (true) {
    var x = 10;
  }
  // x should be accessible here due to var hoisting
  console.log(x); // Expected: 10
}
```

In JavaScript, `var` declarations are function-scoped (or globally-scoped), not block-scoped, so they should be hoisted to the containing function scope. However, it appears that the variable is not being made available outside the block where it was declared.

### Expected behavior

Variables declared with `var` should be hoisted to the parent function scope and be accessible throughout that scope, regardless of which nested block they were declared in. This is standard JavaScript behavior that differentiates `var` from `let` and `const`.

### Additional context

This seems to affect conflict detection as well - the scope system should be able to detect when a `var` declaration conflicts with variables in parent scopes, but that doesn't seem to be working correctly anymore.

---
Repository: /testbed
