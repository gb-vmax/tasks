# Bug Report

### Describe the bug
When creating a new UnitTestSuite, the `parentId` validation is happening before the document is actually created by `db.docCreate()`. This means that if the `parentId` is supposed to be set by `db.docCreate()` (e.g., through default values or internal logic), the validation will fail even though the final created document would have a valid `parentId`.

### Reproduction
```js
// Attempting to create a UnitTestSuite where parentId is set during docCreate
const suite = create({
  name: 'My Test Suite'
  // parentId might be set by db.docCreate internally
});
```

The error is thrown before `db.docCreate()` has a chance to populate the `parentId`, even if the database layer would have set it correctly.

### Expected behavior
The validation should check the `parentId` on the actual created document (after `db.docCreate()` has processed it), not on the input patch object. This would allow `db.docCreate()` to set default values or apply any transformations before validation occurs.

### Additional context
This affects any code path that relies on `db.docCreate()` to populate required fields rather than passing them explicitly in the patch object.

---
Repository: /testbed
