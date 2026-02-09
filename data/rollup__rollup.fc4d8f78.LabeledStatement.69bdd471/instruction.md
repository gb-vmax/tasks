# Bug Report

### Describe the bug

I'm experiencing an issue with labeled statements in my code. It seems like labels are being incorrectly included or excluded during tree-shaking, which is causing unexpected behavior in the bundled output.

### Reproduction

```js
function test() {
  outer: for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (i === 2 && j === 2) {
        break outer;
      }
      console.log(i, j);
    }
  }
}

test();
```

When bundling code with labeled statements like the above, the label itself appears to be getting stripped out even when it's actually being referenced by a break/continue statement. This results in invalid output code or the label not being present when it should be.

### Expected behavior

Labeled statements should be properly preserved in the output when they are referenced by break or continue statements within their scope. The bundler should correctly detect when a label is actually being used and include it accordingly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
