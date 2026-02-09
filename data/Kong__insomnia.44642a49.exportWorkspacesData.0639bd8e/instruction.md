# Bug Report

### Describe the bug

When exporting workspaces, the exported data appears to be missing all requests. Instead of including HTTP requests, gRPC requests, and WebSocket requests in the export, they seem to be completely excluded from the output file.

### Reproduction

1. Create a workspace with several requests (HTTP, gRPC, WebSocket)
2. Use the export functionality to export the workspace data
3. Check the exported file

### Expected behavior

The exported file should contain all requests from the workspace, including:
- HTTP requests
- gRPC requests  
- WebSocket requests

Instead, the export seems to be filtering out these request types rather than including them.

### System Info

- Insomnia version: latest
- Export format: both JSON and YAML affected

---
Repository: /testbed
