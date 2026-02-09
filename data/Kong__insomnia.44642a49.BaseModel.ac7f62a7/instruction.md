# Bug Report

### Describe the bug

When duplicating documents with children in the database, the duplicated children are being linked to the wrong parent. Instead of being linked to the newly created parent document, they're being linked back to the original parent document.

### Reproduction

```js
// 1. Create a parent document
const parentDoc = await database.insert({
  _id: 'parent_1',
  type: 'request_group',
  name: 'Parent Folder'
});

// 2. Create a child document
const childDoc = await database.insert({
  _id: 'child_1',
  type: 'request',
  parentId: 'parent_1',
  name: 'Child Request'
});

// 3. Duplicate the parent
const duplicatedParent = await database.duplicate(parentDoc, {
  name: 'Duplicated Parent Folder'
});

// 4. Check the duplicated child's parent
const duplicatedChildren = await database.find('request', { 
  parentId: duplicatedParent._id 
});

console.log(duplicatedChildren.length); // Expected: 1, Actual: 0
```

The child document is not properly associated with the duplicated parent. When you try to find children of the duplicated parent, you get an empty array because the duplicated child still references the original parent ID instead of the new parent ID.

### Expected behavior

When duplicating a document that has children, the duplicated children should reference the newly created parent document's ID, not the original parent's ID. The entire hierarchy should be properly recreated with new IDs while maintaining the parent-child relationships.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
