# Bug Report

### Describe the bug

While loops with side effects in the test condition are being incorrectly tree-shaken/removed from the output bundle. The loop body is being included even when it should be excluded, and vice versa.

### Reproduction

```js
let count = 0;

// This while loop should be preserved because the test has side effects
while (sideEffect()) {
  doSomething();
}

function sideEffect() {
  count++;
  return count < 5;
}

function doSomething() {
  console.log('executed');
}
```

After bundling, the while loop behavior is inverted - loops that should be kept are removed and loops without effects are incorrectly preserved.

### Expected behavior

While loops should be included in the bundle when:
1. The test condition has side effects, OR
2. The loop body has side effects

The current behavior seems to have the logic reversed for determining whether the loop body has effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
