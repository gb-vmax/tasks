# Bug Report

### Describe the bug

When using optional chaining in my code, the build process hangs indefinitely and eventually crashes with a "Maximum call stack size exceeded" error. This seems to happen specifically when processing code that contains optional chaining expressions (`?.`).

### Reproduction

```js
// Example code that causes the issue
const obj = {
  nested: {
    value: 42
  }
}

const result = obj?.nested?.value;
```

When trying to bundle this code, the build process freezes and eventually fails with a stack overflow error.

### Expected behavior

The code should bundle successfully without hanging or crashing. Optional chaining expressions should be processed normally during the build.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
