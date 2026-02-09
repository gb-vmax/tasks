# Bug Report

### Describe the bug

When duplicating documents with nested children, the children are not being properly associated with the newly duplicated parent document. Instead, they appear to remain linked to the original parent.

### Reproduction

```js
// 1. Create a parent document
const parentDoc = await database.insert({
  _id: 'parent_1',
  type: 'Request',
  name: 'Parent Request'
});

// 2. Create a child document
const childDoc = await database.insert({
  _id: 'child_1',
  type: 'RequestHeader',
  parentId: 'parent_1',
  name: 'Authorization Header'
});

// 3. Duplicate the parent
const duplicatedParent = await database.duplicate(parentDoc);

// 4. Check the child's parent
const duplicatedChildren = await database.find('RequestHeader', { 
  parentId: duplicatedParent._id 
});

// Expected: duplicatedChildren.length === 1
// Actual: duplicatedChildren.length === 0
// The child is still pointing to the original parent
```

### Expected behavior

When duplicating a document that has children, the duplicated children should reference the new parent document's ID, not the original parent's ID. The entire hierarchy should be properly replicated with updated parent-child relationships.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
