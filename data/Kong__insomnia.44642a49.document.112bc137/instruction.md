# Bug Report

### Describe the bug

I'm experiencing an issue with the status candidate schema where the `document` field seems to be caching values unexpectedly across different contexts. When I create multiple status candidates, they sometimes share the same document instance even though they should have separate documents.

### Reproduction

```js
// Create first status candidate
const candidate1 = {
  key: 'key1',
  name: 'Candidate 1',
  document: statusCandidateSchema.document()
};

// Create second status candidate
const candidate2 = {
  key: 'key2', 
  name: 'Candidate 2',
  document: statusCandidateSchema.document()
};

// Both candidates end up with the same document reference
console.log(candidate1.document === candidate2.document); // true (unexpected!)
```

### Expected behavior

Each status candidate should get its own unique document instance. The documents should not be shared between different candidates unless explicitly intended.

### Additional context

This seems to be affecting sync operations where multiple status candidates are being processed. The shared document state is causing data to leak between candidates.

Not sure if this is related to recent changes in the schema system, but it wasn't happening in previous versions.

---
Repository: /testbed
