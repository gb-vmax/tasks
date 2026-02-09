# Bug Report

### Describe the bug

I've encountered an issue with while loops where the loop condition is not being evaluated correctly during tree-shaking. It seems like the test expression in while statements is being processed in the wrong order, which can lead to incorrect code elimination.

### Reproduction

```js
// Input code
let x = 0;
while (sideEffect()) {
  x++;
}
console.log(x);
```

When bundling this code, the side effects from the while loop's test condition aren't being tracked properly. The condition should be evaluated before the loop body is included, but it appears to be happening in reverse order.

### Expected behavior

The while loop's test expression should be included and evaluated before the loop body to ensure proper side effect tracking and tree-shaking. The current behavior may cause the bundler to incorrectly eliminate or include code based on an improper evaluation order.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
