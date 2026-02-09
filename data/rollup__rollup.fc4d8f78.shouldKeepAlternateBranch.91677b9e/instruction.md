# Bug Report

### Describe the bug

I'm experiencing an issue with nested if-else statements where the else branches are being incorrectly removed during tree-shaking/dead code elimination. When I have an if statement inside another if statement's consequent branch (the "then" part), the outer else branch gets eliminated even though it should be preserved.

### Reproduction

```js
function test(x, y) {
  if (x) {
    if (y) {
      console.log('both true');
    }
  } else {
    console.log('x is false');
  }
}
```

After bundling, the outer `else` branch (`console.log('x is false')`) is being removed from the output, which breaks the logic when `x` is false.

### Expected behavior

The else branch should be preserved in the bundled output since it's reachable code. When `x` is false, the function should log 'x is false', but currently it doesn't execute anything in that case.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to be affecting any nested if-statement patterns where you have an if inside the consequent branch of another if statement that also has an alternate branch.

---
Repository: /testbed
