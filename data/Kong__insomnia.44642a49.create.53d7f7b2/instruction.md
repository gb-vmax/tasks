# Bug Report

### Describe the bug

I'm encountering an issue when creating new request metadata. The `create()` function seems to be broken and is not properly handling the patch object that's passed to it.

### Reproduction

```js
import { create } from './request-meta';

// Try to create request metadata with valid data
const meta = create({
  parentId: 'req_123',
  downloadPath: '/some/path',
  responseFilter: 'body'
});

// Expected: Creates a new RequestMeta with all the provided properties
// Actual: Only parentId is passed, other properties are lost
```

When calling `create()` with a patch object containing multiple properties, only the `parentId` seems to be used and all other properties in the patch are ignored.

### Expected behavior

The `create()` function should accept a patch object with various RequestMeta properties (like `downloadPath`, `responseFilter`, etc.) and create a new RequestMeta document with all those properties included, not just the `parentId`.

### Additional context

This appears to have broken recently. Previously the function was working correctly and would merge all patch properties into the created document.

---
Repository: /testbed
