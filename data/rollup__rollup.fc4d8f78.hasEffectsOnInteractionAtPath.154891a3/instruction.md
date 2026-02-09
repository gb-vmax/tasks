# Bug Report

### Describe the bug

I'm encountering an issue with string literal side effect detection. When accessing properties on string literals, the tree-shaking behavior seems incorrect - it's treating direct property access as having side effects when it shouldn't.

### Reproduction

```js
const str = "hello";
const result = str.length;  // This should be side-effect free but is being flagged
```

Similarly, when calling methods on string literals:

```js
const str = "test";
const upper = str.toUpperCase();  // Method calls are being incorrectly analyzed
```

The bundler is not properly optimizing these expressions during the tree-shaking phase. It appears that accessing properties directly on string literals is being treated as having side effects, which prevents proper dead code elimination.

### Expected behavior

- Direct property access on string literals (like `.length`) should be recognized as side-effect free
- String method calls should only be checked for side effects when they're actually being invoked on nested paths

This is affecting bundle size optimization in my project since perfectly safe string operations are being preserved unnecessarily.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
