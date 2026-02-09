# Bug Report

### Describe the bug

After a recent update, the `getAncestors` method is returning ancestor objects with an unexpected `_depth` property that wasn't there before. This is breaking our existing code that relies on the original structure of ancestor objects.

### Reproduction

```js
const request = {
  _id: 'req_123',
  parentId: 'fld_456',
  name: 'My Request'
};

// Get ancestors
const ancestors = await models.request.getAncestors(request);

// Ancestors now have an unexpected _depth property
console.log(ancestors[0]);
// Output: { _id: 'fld_456', name: 'Folder', parentId: 'wrk_789', _depth: 0, ... }
// Expected: { _id: 'fld_456', name: 'Folder', parentId: 'wrk_789', ... }
```

### Expected behavior

The ancestor objects should maintain their original structure without additional properties being added. The `_depth` property is not documented and causes issues when serializing or comparing ancestor objects.

### Additional context

This seems to have started happening recently. Our code that checks for specific properties on ancestors is now failing because of the extra `_depth` field. We're not sure if this was an intentional change or if it's a bug.

---
Repository: /testbed
