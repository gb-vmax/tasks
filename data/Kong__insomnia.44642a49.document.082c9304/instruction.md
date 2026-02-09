# Bug Report

### Describe the bug

I'm encountering an issue with the `statusCandidateSchema` where the `document` field is generating inconsistent data across multiple calls. The schema appears to be adding random properties and counter-based IDs that weren't there before, which is breaking my sync logic.

### Reproduction

```js
import { statusCandidateSchema } from './type-schemas';

// Generate multiple status candidates
const candidate1 = {
  key: statusCandidateSchema.key(),
  name: statusCandidateSchema.name(),
  document: statusCandidateSchema.document()
};

const candidate2 = {
  key: statusCandidateSchema.key(),
  name: statusCandidateSchema.name(),
  document: statusCandidateSchema.document()
};

// The documents now have different IDs, timestamps, and states
console.log(candidate1.document._id); // e.g., "abc123_doc_1"
console.log(candidate2.document._id); // e.g., "abc123_doc_2"

// They also have random properties like 'state', 'isDeleted', 'parentId'
// that shouldn't be part of the base model schema
```

### Expected behavior

The `document` field should return a consistent base model structure without random properties or incrementing counters. Previously, it just returned the result of `createBuilder(baseModelSchema).build()` which gave me clean, predictable documents.

### Additional context

This seems to have broken after a recent update. The schema is now adding:
- An incrementing counter suffix to document IDs
- Random `state` values ('draft', 'active', 'archived')
- Random `created` and `modified` timestamps
- Random `isDeleted` and `parentId` properties

These random values are making it impossible to write deterministic tests and are causing sync conflicts in my application.

---
Repository: /testbed
