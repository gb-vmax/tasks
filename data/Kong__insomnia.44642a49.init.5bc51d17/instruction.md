# Bug Report

### Describe the bug

When creating a new Proto File, the initial values for `name` and `protoText` are not set correctly. The `name` field is `undefined` instead of having a default string value, and `protoText` is `null` instead of an empty string.

### Reproduction

```js
const newProtoFile = init();

console.log(newProtoFile.name); // Expected: 'New Proto File', Actual: undefined
console.log(newProtoFile.protoText); // Expected: '', Actual: null
```

### Expected behavior

When initializing a new Proto File:
- The `name` property should default to `'New Proto File'`
- The `protoText` property should default to an empty string `''`

This is causing issues when trying to display or work with newly created proto files, as the UI expects these fields to have string values rather than `undefined` or `null`.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
