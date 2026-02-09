# Bug Report

### Describe the bug

I'm experiencing an issue where `getById()` is returning undefined for proto files that definitely exist in the database. The function appears to be failing to retrieve proto files by their ID even when the ID is correct.

### Reproduction

```js
// Create or get a proto file with a valid ID
const protoFileId = 'proto_abc123';

// Try to retrieve it by ID
const protoFile = getById(protoFileId);

// protoFile is undefined even though the file exists
console.log(protoFile); // undefined
```

### Expected behavior

The `getById()` function should return the proto file object when a valid ID is provided. Previously this was working correctly, but now it's consistently returning undefined.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
