# Bug Report

### Describe the bug

I'm experiencing infinite recursion when building my project. The build process hangs and eventually crashes with a stack overflow error. This seems to happen during the code generation phase.

### Reproduction

```js
// Simple expression statement that triggers the issue
const result = someFunction();
```

When this code is processed during bundling, the build never completes and the process consumes increasing amounts of memory until it crashes.

### Expected behavior

The build should complete successfully without hanging or crashing. Expression statements should be processed normally during the annotation removal phase.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

The build was working fine before, but now it consistently hangs on the same files. I've tried clearing caches and reinstalling dependencies but the issue persists.

---
Repository: /testbed
