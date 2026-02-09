# Bug Report

### Describe the bug

After a recent update, gRPC proto file loading is completely broken. When trying to load methods from a proto file, the application crashes or hangs without any error message. This affects all gRPC requests that rely on proto file definitions.

### Reproduction

1. Open Insomnia
2. Create a new gRPC request
3. Try to load a proto file to define the service methods
4. The proto file fails to load and no methods are displayed

Alternatively, if using the API directly:
```js
// Attempt to load methods from a proto file
const methods = await loadMethodsFromFilePath('/path/to/service.proto', ['/path/to/includes']);
// This never completes or returns undefined
```

### Expected behavior

The proto file should load successfully and all available gRPC methods should be displayed in the UI. Previously this was working fine and would parse the proto file and return the method definitions.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking all gRPC development work. Any help would be appreciated!

---
Repository: /testbed
