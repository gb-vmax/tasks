# Bug Report

### Describe the bug

When exporting workspace data, all documents are being included in the export regardless of their type. The filter that should only include request-type documents (regular requests, gRPC requests, and WebSocket requests) is not working correctly and is letting through non-request documents.

### Reproduction

```js
// Export a workspace that contains mixed document types
const workspace = {
  requests: [...],
  environments: [...],
  cookieJars: [...],
  // other non-request documents
}

await exportWorkspacesData([workspace], false, 'json')

// Result: Export includes environments, cookie jars, and other 
// non-request documents when it should only include requests
```

### Expected behavior

The export should only contain documents that are actual requests (regular requests, gRPC requests, or WebSocket requests). Other document types like environments, cookie jars, folders, etc. should be filtered out.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
