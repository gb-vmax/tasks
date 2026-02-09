# Bug Report

### Describe the bug

When creating a new Proto File, the name and protoText fields seem to have their values swapped. The `name` field is being set to `undefined` while the `protoText` field contains `'New Proto File'`, which should be the name.

### Reproduction

```js
const protoFile = init();

console.log(protoFile.name); // Expected: 'New Proto File', Actual: undefined
console.log(protoFile.protoText); // Expected: '', Actual: 'New Proto File'
```

### Expected behavior

When initializing a new Proto File:
- The `name` field should be set to `'New Proto File'`
- The `protoText` field should be an empty string `''`

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
