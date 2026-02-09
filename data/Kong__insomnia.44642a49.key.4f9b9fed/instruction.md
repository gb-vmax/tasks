# Bug Report

### Describe the bug

I'm encountering a syntax error in the type schemas file after a recent update. The code appears to have malformed structure where variable declarations and function definitions are placed outside of the schema object, causing the schema definition to be invalid.

### Reproduction

When trying to use the merge conflict schema, I get a JavaScript syntax error. The schema object structure seems broken:

```js
// The mergeConflictSchema object has invalid syntax
// Variables and functions are declared in the middle of the object definition
// causing the 'key' property to be unreachable
```

Attempting to import or use `mergeConflictSchema` results in parsing errors at runtime.

### Expected behavior

The `mergeConflictSchema` should be a valid JavaScript object with properly defined properties. The schema should be usable without syntax errors.

### System Info
- Node version: 18.x
- Package: insomnia/sync

This seems to have been introduced recently and is blocking my ability to work with merge conflicts in the sync module. Any help would be appreciated!

---
Repository: /testbed
