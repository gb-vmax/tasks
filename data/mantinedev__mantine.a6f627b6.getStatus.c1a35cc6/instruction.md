# Bug Report

### Describe the bug

The form status checking is not working correctly for nested fields. When I check the status of a field that has nested children, it always returns `false` even when the nested fields have a truthy status.

### Reproduction

```js
const status = {
  'user.name': true,
  'user.email': true,
  'user.address.street': true
};

// Checking parent field status
const userStatus = getStatus(status, 'user');
// Returns false, but should return true since nested fields have status

const addressStatus = getStatus(status, 'user.address');
// Also returns false incorrectly
```

### Expected behavior

When checking the status of a parent field (e.g., `'user'`), it should return `true` if any of its nested fields (e.g., `'user.name'`, `'user.email'`, `'user.address.street'`) have a truthy status value.

This was working fine before but seems to have broken recently. The function should detect when nested paths exist and return the appropriate status.

---
Repository: /testbed
