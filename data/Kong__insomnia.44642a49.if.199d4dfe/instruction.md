# Bug Report

### Describe the bug

I'm experiencing an issue with the VCS sync functionality where changes to model properties are not being properly detected. When comparing two versions of a model, certain keys that should be ignored are instead being set to `undefined` in the first object, which is causing incorrect change descriptions.

### Reproduction

```js
const modelA = {
  id: '123',
  name: 'Test',
  _timestamp: 1234567890,
  someProperty: 'value'
};

const modelB = {
  id: '123',
  name: 'Test Updated',
  _timestamp: 9876543210,
  someProperty: 'value'
};

// When describing changes between modelA and modelB,
// properties that should be ignored are being modified in modelA
const changes = describeChanges(modelA, modelB);

// After the call, modelA has been mutated unexpectedly
// modelA._timestamp is now undefined instead of being ignored
```

### Expected behavior

The `describeChanges` function should skip over keys that need to be ignored without modifying the input objects. Properties like timestamps and other metadata should be left untouched in the original objects.

### System Info

- Insomnia version: latest
- OS: macOS

This seems to have started happening recently and is affecting the sync comparison logic. The first object passed to the comparison is being unexpectedly mutated.

---
Repository: /testbed
