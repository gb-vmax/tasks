# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot state entries where the `name` property is being auto-incremented with counters even when I don't expect it. When creating multiple snapshot state entries, the name field gets appended with `-2`, `-3`, etc., which breaks my code that relies on consistent naming.

### Reproduction

```js
const entry1 = snapshotStateEntrySchema.name();
const entry2 = snapshotStateEntrySchema.name();
const entry3 = snapshotStateEntrySchema.name();

console.log(entry1); // Expected: 'name', Got: 'name'
console.log(entry2); // Expected: 'name', Got: 'name-2'
console.log(entry3); // Expected: 'name', Got: 'name-3'
```

The counter seems to persist across calls, which means if I create entries in different parts of my application, they all get different suffixes. This is particularly problematic when:

1. Creating snapshot entries in different modules
2. Expecting consistent naming for comparison/lookup operations
3. Testing - the counter state carries over between test runs

### Expected behavior

The `name()` function should return a consistent value (just `'name'`) similar to how `blob()` and `key()` work in the same schema. If unique names are needed, that should be handled explicitly by the caller, not automatically by the schema.

### Additional context

This appears to have changed recently as my code was working fine before. The counter also doesn't seem to have any way to reset it, so the numbers just keep incrementing throughout the application lifecycle.

---
Repository: /testbed
