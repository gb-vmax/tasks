# Bug Report

### Describe the bug

After a recent update, several core functions in the request-group model have been removed, causing the application to fail when trying to create, update, or retrieve request groups. Functions like `init()`, `create()`, `update()`, `getById()`, `findByParentId()`, `remove()`, and `all()` are no longer available.

### Reproduction

```js
import * as requestGroup from './models/request-group';

// This no longer works - create function is missing
const newGroup = requestGroup.create({
  parentId: 'wrk_123',
  name: 'My Folder'
});

// This also fails - getById is not defined
const group = requestGroup.getById('fld_abc');

// Same issue with other functions
const groups = requestGroup.findByParentId('wrk_123');
requestGroup.update(existingGroup, { name: 'Updated Name' });
```

### Expected behavior

All the standard CRUD operations should be available for request groups:
- `init()` - Initialize a new request group with defaults
- `create()` - Create a new request group
- `update()` - Update an existing request group
- `getById()` - Retrieve a request group by ID
- `findByParentId()` - Find all request groups under a parent
- `remove()` - Delete a request group
- `all()` - Get all request groups

The `isRequestGroup()` type guard and `migrate()` function are also missing.

### System Info
- Version: Latest from main branch
- The only function that seems to remain is `duplicate()` with modified parameters

This is breaking existing code that relies on these functions throughout the application.

---
Repository: /testbed
