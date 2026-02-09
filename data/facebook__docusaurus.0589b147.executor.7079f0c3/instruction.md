# Bug Report

### Describe the bug

I'm experiencing an issue with the processor's async execution flow. When using the processor with a callback-based API (passing a `done` callback), the callback is being invoked even when using the Promise-based API (when `resolve` is defined).

### Reproduction

```js
const processor = unified()
  .use(somePlugin)
  .use(anotherPlugin);

// Using Promise-based API
const result = await processor.process(tree);
// Expected: Promise resolves with result
// Actual: Both Promise resolves AND callback would be invoked if one was passed
```

The issue seems to be that the internal executor logic doesn't properly distinguish between callback mode and Promise mode, leading to potential double execution or unexpected callback invocations.

### Expected behavior

When using the Promise-based API (not passing a `done` callback), only the Promise should resolve. The `done` callback path should only execute when explicitly using the callback-based API.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
