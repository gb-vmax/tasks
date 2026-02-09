# Bug Report

### Describe the bug

I'm encountering a syntax error in the merge conflict schema that's preventing the application from running. It looks like there's a malformed property definition in the `mergeConflictSchema` object that's causing parsing issues.

### Reproduction

The issue appears to be in the `type-schemas.ts` file where the merge conflict schema is defined. When the application tries to load this module, it fails with a syntax error.

```js
// The schema object has an invalid property definition
const mergeConflictSchema = {
  mineBlobContent: () => null,
  theirsBlob: () => null,
  theirsBlobContent: () => null,
  // This line is causing the issue
  () => { return (() => 'message') }
  name: () => 'name',
};
```

### Expected behavior

The schema should be properly defined with valid JavaScript syntax so the module can be loaded without errors. The `message` property should be accessible like the other properties in the schema.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
