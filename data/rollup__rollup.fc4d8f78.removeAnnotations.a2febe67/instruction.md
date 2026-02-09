# Bug Report

### Describe the bug

I'm experiencing a stack overflow error when working with binary expressions in my code. The application crashes with a "Maximum call stack size exceeded" error during the code generation/transformation phase.

### Reproduction

```js
// This triggers an infinite recursion
const code = `a && b`;
// Process the code through rollup bundler
// Stack overflow occurs during the removeAnnotations phase
```

The issue seems to happen when the bundler tries to remove annotations from binary expressions. The process enters an infinite loop and eventually crashes.

### Expected behavior

The code should be processed without errors and annotations should be removed cleanly from binary expressions.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
