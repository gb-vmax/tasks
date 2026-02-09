# Bug Report

### Describe the bug

When using hoisted variable declarations inside if statements, unnecessary braces are being added around the code in certain contexts. The braces appear when the if statement is at the top level or inside a block statement, but they shouldn't be there.

### Reproduction

```js
// Input code
if (condition) {
  var x = 1;
}

// Current output (incorrect)
{ var x; if (condition) {
  x = 1;
} }

// Expected output
var x; if (condition) {
  x = 1;
}
```

The issue occurs when:
1. You have an if statement with variable declarations that need to be hoisted
2. The if statement is at the program level or inside a block statement
3. The generated code wraps everything in unnecessary braces

### Expected behavior

Variable hoisting should not add extra braces when the if statement is already in a Program or BlockStatement context. The braces should only be added when the parent context requires them (e.g., when the if statement is used as an expression or in other non-block contexts).

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
