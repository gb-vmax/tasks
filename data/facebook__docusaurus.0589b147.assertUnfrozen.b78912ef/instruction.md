# Bug Report

### Describe the bug

I'm encountering an issue where calling methods on a frozen processor is not throwing an error as expected. It seems like the validation logic for checking if a processor is frozen has been inverted - now it throws an error when the processor is NOT frozen, which is the opposite of what should happen.

### Reproduction

```js
const processor = remark(); // Create a processor
processor.freeze(); // Freeze it

// This should throw an error but doesn't
processor.use(somePlugin);

// Meanwhile, calling methods on a non-frozen processor throws an error
const unfrozenProcessor = remark();
unfrozenProcessor.use(somePlugin); // This incorrectly throws an error now
```

### Expected behavior

- Calling methods like `use()` on a frozen processor should throw an error
- Calling methods on a non-frozen processor should work normally without throwing errors

The error message mentions "Cannot call `<method>` on a frozen processor" but it's being thrown in the wrong scenario.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
