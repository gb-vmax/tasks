# Bug Report

### Describe the bug

After a recent update, gRPC requests are behaving strangely when they contain metadata or headers. It seems like some internal properties are being persisted when they shouldn't be, and undefined header values are causing issues.

### Reproduction

```js
const grpcRequest = {
  headers: {
    'content-type': 'application/grpc',
    'authorization': undefined,
    'x-custom-header': 'value'
  },
  metadata: {
    _version: 1,
    someField: 'data'
  }
}

// After processing, the request contains unexpected data
// - undefined header values are still present
// - internal _version field appears in metadata
```

### Expected behavior

- Headers with `undefined` values should be filtered out
- Internal metadata fields like `_version` should not be included in the migrated request
- The migration should properly clean up the request object

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
