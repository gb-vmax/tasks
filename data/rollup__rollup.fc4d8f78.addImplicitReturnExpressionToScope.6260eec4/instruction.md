# Bug Report

### Describe the bug

I'm experiencing an issue with implicit return expressions in block statements. When a function has statements but no explicit return statement, the implicit return behavior is not working as expected.

### Reproduction

```js
function testFunction() {
  const x = 1;
  const y = 2;
  // No explicit return statement
}

// The implicit return expression should be handled correctly
// but it seems like the last statement is not being detected properly
```

Another case:

```js
function anotherTest() {
  doSomething();
  doSomethingElse();
  return value; // explicit return at the end
}

// This should NOT add an implicit return expression
// but it seems to be adding one anyway
```

### Expected behavior

- When a block statement has no explicit return at the end, it should add an implicit return expression
- When a block statement already has a return statement as the last statement, it should NOT add an implicit return expression

Currently it seems like the logic is inverted or the last statement is not being accessed correctly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
