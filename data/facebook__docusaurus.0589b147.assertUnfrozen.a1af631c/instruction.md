# Bug Report

### Describe the bug

I'm encountering an issue where calling methods on a frozen processor throws an error unexpectedly. According to the documentation, frozen processors should prevent modifications, but it seems like the behavior is inverted - unfrozen processors are throwing errors instead.

### Reproduction

```js
const processor = remark();

// Create a frozen processor
const frozen = processor().freeze();

// This should throw an error but doesn't
frozen.use(somePlugin);

// Meanwhile, calling methods on an unfrozen processor throws an error
const unfrozen = remark();
unfrozen.use(somePlugin); // This throws: "Cannot call `use` on a frozen processor."
```

### Expected behavior

- Frozen processors should throw errors when attempting to call methods like `use()`, `parse()`, etc.
- Unfrozen processors should allow method calls without throwing errors

The current behavior seems backwards - unfrozen processors are being treated as frozen and vice versa.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
