# Bug Report

### Describe the bug

I'm experiencing an issue with block statement optimization in my rollup build. After a recent update, code that should be tree-shaken is being included in the bundle, and dead code elimination doesn't seem to be working correctly anymore.

### Reproduction

```js
// input.js
function example() {
  if (false) {
    console.log('This should be removed');
    const unused = 'dead code';
  }
  return 'result';
}

export { example };
```

When bundling this code, the dead code inside the `if (false)` block is not being eliminated as expected. The output bundle still contains the unreachable code.

### Expected behavior

Dead code within block statements that can be statically determined as unreachable should be removed during the optimization phase. The bundle should only contain the reachable `return 'result'` statement.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently - my builds were working fine before. The bundle size has increased noticeably because unreachable code is no longer being eliminated.

---
Repository: /testbed
