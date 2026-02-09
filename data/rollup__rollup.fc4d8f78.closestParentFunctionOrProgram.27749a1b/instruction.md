# Bug Report

### Describe the bug

I'm experiencing an issue where the bundler enters an infinite loop when processing certain code patterns. The build process hangs indefinitely and never completes, requiring a force kill of the process.

### Reproduction

```js
function outer() {
  function inner() {
    // nested function
    return 42;
  }
  return inner();
}

const result = outer();
```

When bundling code with nested function declarations like above, the process hangs and becomes unresponsive. This seems to happen specifically when there are multiple levels of function nesting.

### Expected behavior

The bundler should successfully process nested functions and complete the build without hanging.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This is blocking our production builds, any help would be appreciated!

---
Repository: /testbed
