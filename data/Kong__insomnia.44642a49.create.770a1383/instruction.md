# Bug Report

### Describe the bug
When creating a new RequestMeta object, the function is not properly using the provided patch data. The parentId validation logic appears to be inverted, and the patch data is being completely ignored during creation.

### Reproduction
```js
const patch = {
  parentId: 'req_123',
  someOtherField: 'value'
};

// This throws an error even though parentId is provided
const requestMeta = create(patch);

// Additionally, even if it didn't throw, the patch data would be ignored
// and an empty object would be created instead
```

### Expected behavior
- The function should throw an error when `parentId` is **missing** (not when it's present)
- The provided patch data should be passed to `db.docCreate()` to properly initialize the RequestMeta object with the given values

### System Info
- Package: @insomnia/insomnia
- Module: request-meta.ts

This is causing issues when trying to create request metadata with initial values, as the validation is backwards and the data is being discarded.

---
Repository: /testbed
