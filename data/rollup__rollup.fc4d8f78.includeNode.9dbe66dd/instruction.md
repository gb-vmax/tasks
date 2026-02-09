# Bug Report

### Describe the bug

I'm experiencing an infinite loop/stack overflow when bundling code that contains labeled statements. The build process hangs and eventually crashes with a "Maximum call stack size exceeded" error.

### Reproduction

```js
// input.js
function test() {
  myLabel: {
    console.log('test');
    break myLabel;
  }
}
```

When I try to bundle this code, the process hangs indefinitely and then crashes. This wasn't happening in previous versions.

### Expected behavior

The labeled statement should be processed normally during the bundling phase without causing infinite recursion. The build should complete successfully.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
