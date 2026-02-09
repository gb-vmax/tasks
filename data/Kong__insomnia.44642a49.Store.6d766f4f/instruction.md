# Bug Report

### Describe the bug

I'm encountering an issue with the sync store when there are no hooks registered. The deserialization process seems to be failing or behaving unexpectedly when the hooks array is empty.

### Reproduction

```js
const store = new Store();

// No hooks registered
const data = { test: 'value' };
const serialized = await store._serialize('.json', data);
const deserialized = await store._deserialize('.json', serialized);

// Deserialization fails or returns unexpected result
console.log(deserialized);
```

### Expected behavior

The store should handle serialization and deserialization correctly even when no hooks are registered. The data should be serialized to a buffer and then deserialized back to its original form without errors.

### Additional context

This seems to happen specifically when the `_hooks` array is empty. When hooks are present, everything works as expected. It looks like the deserialization logic might be assuming that hooks will always be present or that the value will always be JSON-parseable.

---
Repository: /testbed
