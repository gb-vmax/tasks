# Bug Report

### Describe the bug

I'm experiencing an issue where the processor seems to get stuck in an infinite loop when calling the `freeze()` method. The application becomes unresponsive and eventually crashes or times out.

### Reproduction

```js
const processor = new Processor();

// Add some attachers
processor.use(somePlugin);
processor.use(anotherPlugin);

// This call hangs indefinitely
processor.freeze();
```

### Expected behavior

The `freeze()` method should complete execution after processing all attachers and return the frozen processor instance. The application should remain responsive.

### Additional context

This seems to have started happening recently. When I debug, it looks like the freeze loop is running but never completing. The `freezeIndex` value keeps growing but the loop condition never becomes false.

---
Repository: /testbed
