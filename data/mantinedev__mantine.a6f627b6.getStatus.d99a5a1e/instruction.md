# Bug Report

### Describe the bug

I'm experiencing an issue with form field status checking when using nested paths. The `getStatus` function seems to be incorrectly matching paths that share a common prefix, even when they shouldn't be considered nested.

### Reproduction

```js
const status = {
  'user.name': true,
  'user.nameExtra': false
};

// This incorrectly returns true because 'user.nameExtra' starts with 'user.name'
const result = getStatus(status, 'user.name');
// Expected: true (only checking 'user.name' and its nested fields like 'user.name.first')
// Actual: Matches 'user.nameExtra' as if it were nested under 'user.name'
```

The problem occurs when checking the status of a field path - it's matching other fields that happen to start with the same string, rather than only matching truly nested paths (those that have a dot separator after the parent path).

For example, if I have fields like:
- `address`
- `addressLine2`

Checking the status of `address` incorrectly considers `addressLine2` as a nested field, when they should be treated as separate sibling fields.

### Expected behavior

The status check should only match actual nested paths. A field like `user.nameExtra` should not be considered nested under `user.name` - only paths like `user.name.first` or `user.name.last` should be matched.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
