# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when bundling code that contains variable declarations with initializers. The process hangs and eventually crashes with a stack overflow error.

### Reproduction

```js
// Input code
const myVariable = someFunction();
let anotherVar = { key: 'value' };
var oldStyle = 123;
```

When trying to bundle this code, the process becomes unresponsive and crashes. This seems to happen specifically when variable declarators have an init value assigned to them.

### Expected behavior

The bundler should process variable declarations normally without hanging or crashing. The annotations should be removed correctly during the bundling process.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This wasn't happening in previous versions, so it might be a recent regression. Any help would be appreciated!

---
Repository: /testbed
