# Bug Report

### Describe the bug

I'm encountering an issue where I can call methods on a frozen processor without getting an error. According to the documentation, calling methods like `use()` or `parse()` on a frozen processor should throw an error, but it's not happening.

### Reproduction

```js
const processor = remark();
const frozen = processor.freeze();

// This should throw an error but doesn't
frozen.use(somePlugin);
```

The frozen processor allows method calls when it shouldn't. I expected to get an error message like "Cannot call `use` on a frozen processor" but instead the call goes through silently.

### Expected behavior

When a processor is frozen, any attempt to call methods on it should throw an error with a message telling me to create a new processor instance first.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
