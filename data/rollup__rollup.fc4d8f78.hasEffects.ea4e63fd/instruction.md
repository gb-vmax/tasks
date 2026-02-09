# Bug Report

### Describe the bug

I'm encountering an issue with labeled statements where break statements targeting a label are not being properly handled when determining side effects. The bundler seems to be incorrectly treating code flow after labeled statements.

### Reproduction

```js
function test() {
  outer: {
    if (condition) {
      break outer;
    }
    console.log('This should be reachable');
  }
  console.log('After label');
}
```

When bundling code with labeled blocks and break statements, the control flow analysis appears to be broken. Code that should be considered reachable (because it can be reached when the break statement is not executed) seems to be treated incorrectly.

### Expected behavior

The bundler should correctly track control flow through labeled statements. When a labeled block contains a conditional break statement, code after the break (but still within the label) should still be considered reachable if the break condition might not be met.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
