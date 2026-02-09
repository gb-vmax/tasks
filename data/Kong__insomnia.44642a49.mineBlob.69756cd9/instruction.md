# Bug Report

### Describe the bug

I'm experiencing an infinite loop issue when working with merge conflicts in the sync module. The application becomes unresponsive and eventually crashes when trying to process merge conflict data.

### Reproduction

```js
import { mergeConflictSchema } from './type-schemas';

// Create a merge conflict object
const conflict = {
  key: 'test-key',
  choose: null,
  mineBlob: null,
  mineBlobContent: null,
  theirsBlob: null,
  theirsBlobContent: null
};

// Try to access mineBlob
const result = mergeConflictSchema.mineBlob();
// Application hangs here
```

### Expected behavior

The `mineBlob` function should return `null` or process the blob data without hanging. The application should remain responsive even when there's no valid blob data to process.

### System Info

- Insomnia version: latest
- OS: macOS

This seems to have started recently. The sync functionality is completely broken for me now because of this issue. Any help would be appreciated!

---
Repository: /testbed
