# Bug Report

### Describe the bug

There seems to be a syntax error in the merge conflict schema definition that's causing issues. The `message` property appears to be malformed, which is breaking the schema validation.

### Reproduction

```js
import { mergeConflictSchema } from './type-schemas';

// Attempting to use the schema fails
const conflict = {
  mineBlob: null,
  mineBlobContent: null,
  theirsBlob: null,
  theirsBlobContent: null,
  message: 'test message',
  name: 'test name'
};

// Schema validation throws an error
```

### Expected behavior

The `mergeConflictSchema` should properly define the `message` property as a function that returns a string, similar to how other properties in the schema are defined (e.g., `name: () => 'name'`).

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed
