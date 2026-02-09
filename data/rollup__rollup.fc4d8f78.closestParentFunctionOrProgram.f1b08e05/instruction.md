# Bug Report

### Describe the bug

The bundler enters an infinite loop and hangs indefinitely when processing certain code patterns. The process becomes unresponsive and needs to be force-killed.

### Reproduction

```js
// This code causes the bundler to hang
function outer() {
  const inner = () => {
    return someVariable;
  };
  return inner();
}
```

When trying to bundle files containing nested function expressions or arrow functions, the build process never completes. CPU usage spikes to 100% and stays there until the process is terminated.

### Expected behavior

The bundler should complete the build process normally without hanging, regardless of function nesting patterns.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This is blocking our production builds. Any help would be appreciated!

---
Repository: /testbed
