# Bug Report

### Describe the bug

I'm experiencing an issue with switch statements where variable scoping appears to be completely broken. Variables declared inside switch cases are leaking into the parent scope, and I'm seeing incorrect behavior with block-scoped declarations.

### Reproduction

```js
function test() {
  let x = 1;
  switch (x) {
    case 1:
      let y = 2;
      console.log(y); // Should work
      break;
    case 2:
      console.log(y); // Should error but doesn't
      break;
  }
  console.log(y); // Should error but doesn't
}
```

The variable `y` declared in one case is accessible in other cases and even outside the switch statement entirely. This violates block scoping rules.

### Expected behavior

Variables declared with `let` or `const` inside switch cases should be scoped to that case block only (or the entire switch if not wrapped in braces). They should not be accessible outside the switch statement or in other cases.

### Additional context

This seems to have broken recently. Switch statements should create their own block scope separate from the parent scope, but it looks like something is wrong with how the scope is being initialized.

---
Repository: /testbed
