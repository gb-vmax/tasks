# Bug Report

### Describe the bug

The application crashes with a syntax error when trying to use sync functionality. It appears that the schema definitions have been corrupted with invalid HTML/XML markup instead of proper JavaScript code.

### Reproduction

```js
// Try to use any sync-related functionality
import { snapshotStateEntrySchema } from './sync/__schemas__/type-schemas';

// This will fail to parse
const schema = snapshotStateEntrySchema;
```

### Expected behavior

The schema should be properly defined with valid JavaScript syntax. The `snapshotStateEntrySchema` should have a `name` property that returns a string value, similar to the `blob` and `key` properties.

### System Info
- Insomnia version: Latest
- Node version: 18.x

This looks like the file got corrupted somehow, possibly during a merge or edit. The schema definition contains HTML markup where there should be JavaScript code.

---
Repository: /testbed
