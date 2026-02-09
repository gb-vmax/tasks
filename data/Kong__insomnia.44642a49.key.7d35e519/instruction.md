# Bug Report

### Describe the bug

I'm encountering an issue with the sync schema where all status candidates are being assigned the same key value. When multiple status candidates are created, they all get `'key'` as their key, which causes problems when trying to uniquely identify them.

### Reproduction

```js
const candidate1 = statusCandidateSchema.key();
const candidate2 = statusCandidateSchema.key();

console.log(candidate1); // Expected: unique key, Got: 'key'
console.log(candidate2); // Expected: different unique key, Got: 'key'
// Both candidates have identical keys
```

### Expected behavior

Each status candidate should have a unique key to properly identify and differentiate them. When creating multiple candidates, they should not share the same key value.

### System Info

- Insomnia version: latest
- Sync module affected

---
Repository: /testbed
