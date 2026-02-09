# Bug Report

### Describe the bug

When duplicating documents with nested children, the duplicated children are incorrectly referencing the original parent instead of the newly created parent. This causes the duplicate hierarchy to be broken - all duplicated children end up pointing back to the original parent document rather than forming a proper duplicate tree structure.

### Reproduction

```js
// 1. Create a parent document
const parent = await database.insert({
  _id: 'parent_1',
  type: 'workspace',
  name: 'My Workspace'
});

// 2. Create a child document
const child = await database.insert({
  _id: 'request_1',
  type: 'request',
  parentId: 'parent_1',
  name: 'My Request'
});

// 3. Duplicate the parent
const duplicatedParent = await database.duplicate(parent);

// 4. Check the children
const children = await database.find('request', { parentId: duplicatedParent._id });

// Expected: children array should contain the duplicated request
// Actual: children array is empty, because the duplicated request still has parentId: 'parent_1'
```

### Expected behavior

When duplicating a document with children, the entire hierarchy should be duplicated correctly:
- The parent should get a new `_id`
- All children should also get new `_id` values
- All duplicated children should have their `parentId` updated to reference the new parent's `_id`, not the original parent

Instead, duplicated children maintain a reference to the original parent, breaking the duplicate hierarchy.

### System Info
- Version: Latest
- This affects any nested document structures (workspaces with requests, folders with subfolders, etc.)

---
Repository: /testbed
