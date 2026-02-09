# Bug Report

### Describe the bug

I'm encountering an issue where calling methods on a frozen processor doesn't throw an error as expected. It seems like the processor is allowing method calls even when it should be frozen and preventing modifications.

### Reproduction

```js
const processor = remark();
const frozenProcessor = processor.freeze();

// This should throw an error but doesn't
frozenProcessor.use(somePlugin);
```

When I freeze a processor and then try to call methods like `use()` on it, I expect an error to be thrown telling me that I can't modify a frozen processor. Instead, the call goes through without any errors.

### Expected behavior

Calling methods on a frozen processor should throw an error with a message like:
```
Cannot call `use` on a frozen processor.
Create a new processor first, by calling it: use `processor()` instead of `processor`.
```

The processor should prevent any modifications once it's been frozen.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
