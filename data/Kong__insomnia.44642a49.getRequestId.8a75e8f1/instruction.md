# Bug Report

### Describe the bug

The `getRequestId()` method in the response context is returning unexpected results. After a recent update, it seems like the method is now doing some kind of validation/sanitization on the request ID, but this is breaking functionality when working with certain valid request IDs.

### Reproduction

```js
// Previously this would work fine
const response = {
  parentId: 'my-custom-request-id'
};

const context = init(response);
const requestId = context.getRequestId();

// Now returns empty string instead of the actual ID
console.log(requestId); // Expected: 'my-custom-request-id', Got: ''
```

Another example:
```js
const response = {
  parentId: 'request@123'
};

const context = init(response);
console.log(context.getRequestId()); // Returns '' but should return 'request@123'
```

### Expected behavior

The `getRequestId()` method should return the actual `parentId` value without modification. If the `parentId` exists, it should be returned as-is. Custom request IDs that don't follow specific naming patterns should still be accessible.

### Additional context

This appears to have started after a recent change to the response context. The method used to simply return `response.parentId || ''` which worked correctly for all request ID formats. Now it seems to be filtering out IDs that don't match certain patterns, which is causing issues with existing workflows that use custom ID formats.

---
Repository: /testbed
