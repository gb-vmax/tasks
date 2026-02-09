# Bug Report

### Describe the bug

When creating a new Proto File, the initialization fails and returns `undefined` instead of a proper proto file object. This causes the application to crash when trying to access properties like `name` or `protoText` on the newly created proto file.

### Reproduction

```js
import { init } from './models/proto-file';

// Try to create a new proto file
const newProtoFile = init();

// Attempting to access properties fails
console.log(newProtoFile.name); // TypeError: Cannot read property 'name' of undefined
console.log(newProtoFile.protoText); // Never gets here
```

### Expected behavior

The `init()` function should return a valid proto file object with default values:
- `name` should be set to 'New Proto File'
- `protoText` should be an empty string

Instead, it returns `undefined` which breaks any code that depends on creating new proto files.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
