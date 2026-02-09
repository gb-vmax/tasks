# Bug Report

### Describe the bug

I'm seeing duplicate warnings being emitted during the build process. It looks like the same warning is being shown multiple times for the same code location, which is cluttering the build output and making it harder to identify actual issues.

### Reproduction

```js
// input.js
function foo() {
  eval('console.log("test")');
}

foo();
```

When bundling this code, the warning about `eval` usage appears multiple times instead of just once.

### Expected behavior

Each warning should only be displayed once per occurrence in the source code. The build output should show each unique warning exactly one time.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
