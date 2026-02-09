# Bug Report

### Describe the bug

I'm experiencing an issue with labeled break statements in my code. When using a `break` statement with a label, the control flow analysis seems to be incorrect, causing unexpected behavior during tree-shaking or dead code elimination.

### Reproduction

```js
function testFunction() {
  outerLoop: for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (j === 2) {
        break outerLoop;
      }
      console.log(i, j);
    }
  }
  
  // Code after the labeled break
  console.log('This should execute');
}
```

When bundling code with labeled break statements, the flow analysis appears to incorrectly handle the control flow, potentially leading to:
- Incorrect tree-shaking decisions
- Issues with determining which code is reachable after the break

### Expected behavior

Labeled break statements should be properly tracked during control flow analysis. The bundler should correctly identify:
1. Which labels are being referenced by break statements
2. The flow state after a labeled break is encountered
3. What code is reachable after the break statement

The order of operations when processing labeled breaks seems critical for proper flow analysis.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
