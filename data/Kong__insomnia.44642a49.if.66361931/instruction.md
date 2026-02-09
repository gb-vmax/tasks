# Bug Report

### Describe the bug
After a recent update, I'm unable to modify the `_id` field when updating request objects. It seems like certain fields are now being filtered out during the update operation, which is breaking my workflow where I need to update request IDs in specific scenarios.

### Reproduction
```js
const request = {
  _id: 'req_123',
  name: 'My Request',
  url: 'https://example.com'
};

// Try to update the request with a new ID
await update(request, {
  _id: 'req_456',
  name: 'Updated Request'
});

// The _id field remains 'req_123' instead of being updated to 'req_456'
```

### Expected behavior
When I pass `_id` (or other fields like `created`, `type`, `parentId`) in the patch object, they should be included in the update. Previously this worked fine, but now these fields seem to be silently ignored.

### Additional context
This is affecting my ability to:
- Clone requests with new IDs
- Migrate requests between workspaces
- Update request metadata programmatically

Is this intentional? If these fields need to be protected, could we at least get a warning or error when trying to update them?

---
Repository: /testbed
