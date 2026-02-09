# Bug Report

### Describe the bug

I'm experiencing an issue with loop control flow detection in my bundled code. It seems like `break` and `continue` statements inside loops are being confused with each other, causing incorrect tree-shaking behavior.

### Reproduction

```js
function test() {
  while (true) {
    if (condition1) {
      break;
    }
    doSomething();
  }
  
  for (let i = 0; i < 10; i++) {
    if (condition2) {
      continue;
    }
    doSomethingElse();
  }
}
```

When bundling code like this, the output seems to incorrectly handle the control flow analysis. Code that should be included/excluded based on whether loops contain `break` or `continue` statements is being processed incorrectly.

### Expected behavior

The bundler should correctly distinguish between `break` and `continue` statements when analyzing loop control flow. Code reachability analysis should work properly for both types of loop control statements.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like it might be related to how the AST traversal handles loop body inclusion and control flow state management.

---
Repository: /testbed
