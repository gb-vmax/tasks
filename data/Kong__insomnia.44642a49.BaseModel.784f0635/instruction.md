# Bug Report

### Describe the bug

When duplicating documents with nested children, the duplicated children are being assigned to the wrong parent. Instead of being assigned to the newly created parent document, they're being assigned back to the original parent.

### Reproduction

```js
// 1. Create a parent document
const parentDoc = await database.duplicate(originalParent);

// 2. Check the children of the duplicated parent
const children = await database.find('SomeChildType', { parentId: parentDoc._id });

// Expected: children array should contain the duplicated children
// Actual: children array is empty, duplicated children still reference original parent
```

### Steps to reproduce:
1. Create a document with nested children (e.g., a folder with requests)
2. Use the duplicate function to duplicate the parent document
3. Query for children using the new parent's ID
4. The children are not found because they still reference the original parent ID

### Expected behavior

When duplicating a document with children, the duplicated children should have their `parentId` set to the newly created parent document's `_id`, not the original parent's `_id`.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like a regression as document duplication was working correctly before. The duplicated hierarchy is broken because child documents aren't properly linked to their new parent.

---
Repository: /testbed
