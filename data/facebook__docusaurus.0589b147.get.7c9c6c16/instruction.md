# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when using the remark-mdx library. The application crashes with a "Maximum call stack size exceeded" error during module initialization or when certain MDX features are being processed.

### Reproduction

The issue occurs when the library attempts to copy properties between objects. It seems to happen during the module loading phase, making it difficult to isolate, but it consistently crashes with a stack overflow error.

```js
// This triggers the infinite recursion
import remarkMdx from 'remark-mdx';

// Application crashes before any code can execute
```

### Expected behavior

The library should initialize without errors and properly copy properties from source objects to target objects without causing infinite recursion.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest
- Browser: N/A (occurs during build/runtime initialization)

This appears to have started happening recently. The error makes it impossible to use the library at all.

---
Repository: /testbed
