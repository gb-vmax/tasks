# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot state entries where multiple entries end up with the same key value. When creating or processing multiple snapshot state entries, they all get assigned the key `'key'` instead of having unique identifiers.

### Reproduction

```js
// Creating multiple snapshot state entries
const entry1 = createSnapshotStateEntry();
const entry2 = createSnapshotStateEntry();
const entry3 = createSnapshotStateEntry();

// All entries have the same key
console.log(entry1.key); // 'key'
console.log(entry2.key); // 'key'
console.log(entry3.key); // 'key'
```

This causes problems when trying to store or look up entries since they can't be distinguished from each other.

### Expected behavior

Each snapshot state entry should have a unique key value so they can be properly identified and managed separately.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
