# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations in function scopes. When I declare a `let` or `const` variable with the same name as an existing `var` or function declaration, the code doesn't throw an error as expected. The redeclaration seems to be silently allowed instead of being flagged as invalid.

### Reproduction

```js
function test() {
  var x = 1;
  let x = 2; // This should throw an error but doesn't
  console.log(x);
}

function example() {
  function foo() {}
  const foo = 'bar'; // This should also throw an error
}
```

### Expected behavior

Redeclaring a variable with `let` or `const` when a `var` or `function` declaration already exists in the same function scope should be treated as an error. The behavior should follow standard JavaScript scoping rules where `let`/`const` cannot redeclare existing bindings.

Currently, it seems like all declaration kinds are being treated the same way and allowed to redeclare each other, which is incorrect.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
