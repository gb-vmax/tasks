# Bug Report

### Describe the bug

After a recent update, gRPC method loading is completely broken. When trying to load proto files, the application fails to properly handle errors and the methods aren't being returned correctly.

### Reproduction

```js
// Try to load methods from a proto file
const methods = await loadMethodsFromFilePath('/path/to/service.proto', ['/path/to/includes']);

// Expected: Should return array of gRPC methods or throw a proper error
// Actual: Function doesn't return anything or returns undefined
```

### Steps to reproduce:
1. Create a gRPC request with a proto file
2. Try to load the methods from the proto file
3. Notice that the method list doesn't populate

### Expected behavior

The function should either:
- Return the list of gRPC methods from the proto file definition
- Throw an error if the proto file cannot be loaded

Currently it seems like the function flow is broken and doesn't reach the return statement properly.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
