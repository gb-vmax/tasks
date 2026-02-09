# Bug Report

### Describe the bug

I'm experiencing an issue with the snapshot state entry schema where the `key` field is returning an object instead of a string value. This is causing problems when the key is used in operations that expect a string.

### Reproduction

```js
const entry = snapshotStateEntrySchema.key();
console.log(typeof entry); // Expected: 'string', Actual: 'object'
console.log(entry); // Returns an object with toString and valueOf methods
```

When trying to use the key directly in string operations or comparisons, it doesn't behave as expected since it's wrapped in an object rather than being a plain string.

### Expected behavior

The `key` field should return a simple string value `'key'` directly, not an object with `toString` and `valueOf` methods. This would be consistent with how the `blob` and `name` fields work in the same schema.

### System Info
- Package: insomnia
- Module: sync/__schemas__/type-schemas.ts

---
Repository: /testbed
