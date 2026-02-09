# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot state entries where the `key` field is no longer generating consistent values. After a recent update, it seems like the key generation has changed and is now producing sequential keys like `key-1`, `key-2`, etc. instead of the static value.

This is causing problems when trying to compare or match snapshot entries, as the keys are now different across different runs or operations even for the same data.

### Reproduction

```js
// Create multiple snapshot state entries
const entry1 = snapshotStateEntrySchema.key();
const entry2 = snapshotStateEntrySchema.key();

console.log(entry1); // Outputs: key-1
console.log(entry2); // Outputs: key-2

// If I create another entry later
const entry3 = snapshotStateEntrySchema.key();
console.log(entry3); // Outputs: key-3
```

The keys keep incrementing instead of returning a consistent value. This makes it impossible to reliably identify or match entries.

### Expected behavior

The `key` field should generate consistent, predictable values that can be used to identify snapshot state entries. Previously it was returning a static `'key'` value which was more predictable for testing and comparison purposes.

### Additional context

This appears to have introduced a global counter that persists across different operations, which means the key values depend on the order and number of times the schema is accessed, rather than being deterministic.

---
Repository: /testbed
