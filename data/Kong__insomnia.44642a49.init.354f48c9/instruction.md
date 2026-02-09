# Bug Report

### Describe the bug
When creating a new Proto File, the default name is now empty instead of having a descriptive default value. This makes it difficult to distinguish between newly created proto files in the UI, especially when multiple files are created at once.

### Reproduction
```js
// Create a new proto file
const protoFile = init();

// Expected: protoFile.name === 'New Proto File'
// Actual: protoFile.name === ''
```

Steps to reproduce:
1. Create a new proto file using the init() function
2. Check the name property
3. The name is an empty string instead of 'New Proto File'

### Expected behavior
New proto files should have a default name like 'New Proto File' to make them easily identifiable in the UI before the user renames them. An empty name makes it confusing when working with multiple proto files.

### Additional context
Also noticed that `protoText` now defaults to a single space `' '` instead of an empty string `''`, which seems inconsistent with the typical empty state pattern.

---
Repository: /testbed
