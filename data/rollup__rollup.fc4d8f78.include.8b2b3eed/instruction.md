# Bug Report

### Describe the bug

I'm experiencing an issue with do-while loops where the loop body is not being included properly in the output bundle. It seems like the code inside do-while statements is being incorrectly tree-shaken even when it should be preserved.

### Reproduction

```js
// Input code
let counter = 0;
do {
  console.log('This should be included');
  counter++;
} while (counter < 3);
```

When bundling this code, the loop body appears to be missing or not properly included in certain scenarios. The do-while structure is there but the actual statements inside the loop seem to get stripped out when they shouldn't be.

### Expected behavior

The entire do-while loop, including all statements in the body, should be preserved in the output bundle when the loop is determined to have side effects or is otherwise needed.

### Additional context

This seems to affect specifically do-while loops. Regular while loops and for loops don't exhibit this behavior. The issue might be related to how the AST nodes are being traversed during the inclusion phase.

---
Repository: /testbed
