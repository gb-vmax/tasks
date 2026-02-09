# Bug Report

### Describe the bug

When duplicating a document with nested children, the child documents are not being properly associated with the newly created parent. Instead, they seem to be getting linked back to the original parent document.

### Reproduction

```js
// 1. Create a parent document
const parentDoc = await database.insert({
  _id: 'parent_1',
  type: 'RequestGroup',
  name: 'Original Parent'
});

// 2. Create a child document under the parent
const childDoc = await database.insert({
  _id: 'request_1',
  type: 'Request',
  name: 'Child Request',
  parentId: 'parent_1'
});

// 3. Duplicate the parent
const duplicatedParent = await database.duplicate(parentDoc);

// 4. Check the children of the duplicated parent
const duplicatedChildren = await database.find('Request', { 
  parentId: duplicatedParent._id 
});

console.log(duplicatedChildren.length); // Expected: 1, but getting 0
```

### Expected behavior

When duplicating a parent document, all of its children should also be duplicated and linked to the new parent document (not the original parent). The duplicated children should have the `parentId` pointing to the newly created parent's `_id`.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our workflow where we need to duplicate entire request groups with all their nested requests.

---
Repository: /testbed
