# Bug Report

### Describe the bug

I'm experiencing an issue with the processor initialization where transformers seem to be getting overwritten during construction. After creating a new processor instance, the transformers property is set to an empty array instead of being properly initialized with `trough()`.

### Reproduction

```js
const processor = new Processor();

// Expected: transformers should be a trough instance with pipeline methods
// Actual: transformers is just an empty array []

// This breaks when trying to use the processor
processor.use(somePlugin); // Fails because array doesn't have the expected methods
```

### Expected behavior

The `transformers` property should remain as a `trough()` instance to maintain the proper pipeline functionality. It should not be overwritten with an empty array during initialization.

### Additional context

This appears to have started happening recently. The processor construction seems to be initializing `transformers` twice - first correctly with `trough()` and then immediately overwriting it with an empty array. This breaks the entire plugin pipeline system.

---
Repository: /testbed
