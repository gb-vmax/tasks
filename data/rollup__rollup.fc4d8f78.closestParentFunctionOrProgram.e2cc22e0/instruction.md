# Bug Report

### Describe the bug

I'm experiencing an issue where the bundler seems to get stuck in an infinite loop or crashes when processing certain function expressions. This appears to happen specifically with arrow functions or function expressions that are deeply nested within the code structure.

### Reproduction

```js
// Example code that triggers the issue
const obj = {
  method: () => {
    const nested = function() {
      return () => {
        // deeply nested function
      }
    }
  }
}
```

When trying to bundle code with nested function expressions like this, the process hangs indefinitely or eventually crashes without producing output.

### Expected behavior

The bundler should correctly process nested function expressions and arrow functions without hanging or crashing.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently - the same code bundled fine in earlier versions. Any ideas what might be causing this?

---
Repository: /testbed
