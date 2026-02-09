# Bug Report

### Describe the bug

When duplicating documents with names like "Request (Copy 2)", the duplicate naming logic doesn't work correctly. The newly duplicated document gets an incorrect name instead of incrementing the copy number properly.

### Reproduction

```js
// Start with a document named "Request (Copy 2)"
const original = {
  _id: 'req_123',
  type: 'Request',
  name: 'Request (Copy 2)',
  parentId: 'folder_1'
};

// Duplicate it
const duplicated = await database.duplicate(original);

// Expected: duplicated.name should be "Request (Copy 3)"
// Actual: The name is not generated correctly
console.log(duplicated.name);
```

The issue seems to happen when:
1. You have a document with a name that already contains "(Copy N)" where N is a number
2. You try to duplicate that document
3. The new duplicate doesn't get the next sequential number

This is particularly problematic when you duplicate something multiple times in a row - the naming pattern breaks down and you end up with confusing duplicate names.

### Expected behavior

When duplicating a document named "Request (Copy 2)", the duplicate should be named "Request (Copy 3)". Similarly:
- "Request (Copy)" → "Request (Copy 2)"
- "Request (Copy 3)" → "Request (Copy 4)"
- etc.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
