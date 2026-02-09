# Bug Report

### Describe the bug

Top-level await detection is not working correctly. When using `await` at the top level of a module (outside of any function), the bundler is not properly recognizing it as top-level await.

### Reproduction

```js
// module.js
const data = await fetch('/api/data');
export { data };
```

The above code should be detected as using top-level await, but it seems like the detection logic is inverted - it's only marking await expressions that are *inside* functions as top-level await, when it should be the opposite.

### Expected behavior

When `await` is used at the module's top level (not inside any function or arrow function), `usesTopLevelAwait` should be set to `true`. Await expressions that are inside function bodies should not be considered top-level await.

### Additional context

This appears to affect module format detection and could cause issues with bundling modules that legitimately use top-level await.

---
Repository: /testbed
