# Bug Report

### Describe the bug
When creating a new gRPC request, all properties from the patch object are being ignored except for `parentId`. This means that if you try to create a gRPC request with custom properties (like `url`, `protoFileId`, `method`, etc.), they won't be included in the created document.

### Reproduction
```js
import * as models from './grpc-request';

// Try to create a gRPC request with custom properties
const newRequest = await models.create({
  parentId: 'wrk_123',
  url: 'grpc://localhost:50051',
  protoFileId: 'proto_456',
  method: 'myService/myMethod'
});

// Expected: newRequest should have all the properties
// Actual: newRequest only has parentId, all other properties are missing
console.log(newRequest.url); // undefined
console.log(newRequest.protoFileId); // undefined
console.log(newRequest.method); // undefined
```

### Expected behavior
The `create` function should accept and apply all properties from the patch object, not just `parentId`. When creating a gRPC request with additional properties, those properties should be present in the created document.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
