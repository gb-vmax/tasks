# Bug Report

### Describe the bug

After updating proto file handling, I'm experiencing an issue where proto file names are being unexpectedly modified. When a proto file name has leading or trailing whitespace, it gets trimmed automatically, which is causing problems with file identification and matching.

### Reproduction

```js
const protoFile = {
  name: '  MyProtoFile  ',
  protoText: 'syntax = "proto3";\n\nmessage Test {}\n',
  type: 'ProtoFile',
  parentId: 'wrk_123'
}

// After migration/processing
// Expected: name remains '  MyProtoFile  '
// Actual: name becomes 'MyProtoFile'
```

### Steps to reproduce:
1. Create a proto file with whitespace in the name (leading or trailing spaces)
2. Process/save the proto file
3. The whitespace gets stripped from the name

This is breaking our workflow where we intentionally use whitespace for formatting/organization purposes. The name should be preserved as-is without automatic trimming.

### Expected behavior
Proto file names should be preserved exactly as entered, including any whitespace characters.

### System Info
- Version: Latest
- Using proto file models with migration system

---
Repository: /testbed
