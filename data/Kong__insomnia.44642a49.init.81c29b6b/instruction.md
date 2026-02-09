# Bug Report

### Describe the bug

When creating a new Proto File, the `name` and `protoText` fields are being initialized as `undefined` and `null` respectively, instead of having proper default values. This causes issues when trying to work with newly created proto files.

### Reproduction

```js
// Create a new proto file
const protoFile = init();

// Expected: protoFile.name should be 'New Proto File'
// Actual: protoFile.name is undefined

// Expected: protoFile.protoText should be ''
// Actual: protoFile.protoText is null
```

Steps to reproduce:
1. Create a new proto file using the `init()` function
2. Check the `name` property - it's `undefined` instead of a default name
3. Check the `protoText` property - it's `null` instead of an empty string

### Expected behavior

New proto files should be initialized with sensible defaults:
- `name` should be set to a default string like 'New Proto File'
- `protoText` should be an empty string `''` rather than `null`

This breaks any code that expects these fields to always be strings and doesn't handle `undefined`/`null` values.

---
Repository: /testbed
