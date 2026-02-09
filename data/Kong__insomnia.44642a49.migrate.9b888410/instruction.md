# Bug Report

### Describe the bug

After a recent update, gRPC request metadata is getting corrupted. When loading existing gRPC requests, the metadata structure appears to be malformed with duplicate/nested data that breaks the request configuration.

### Reproduction

1. Create a gRPC request with some metadata
2. Save the request
3. Reload/reopen the request
4. The metadata structure is now incorrect - it appears to have an extra layer of nesting with both `data` and `meta` properties

The metadata object seems to be getting wrapped in an unexpected structure instead of being returned as-is.

### Expected behavior

The gRPC request metadata should maintain its original structure when loaded. The migrate function should only transform the data when actual migration is needed, not wrap valid metadata in additional layers.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
