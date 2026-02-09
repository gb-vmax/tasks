# Bug Report

### Describe the bug

When creating new gRPC requests, they are automatically pinned and have their `lastActive` timestamp set to the current time. This is unexpected behavior - new requests should start unpinned with a `lastActive` value of 0, similar to how other request types work.

### Reproduction

1. Create a new gRPC request in the application
2. Check the request metadata
3. Observe that `pinned` is set to `true` instead of `false`
4. Observe that `lastActive` has a timestamp instead of being 0

### Expected behavior

New gRPC requests should be initialized with:
- `pinned: false` (not pinned by default)
- `lastActive: 0` (no activity yet)

This would make gRPC requests consistent with other request types and prevent them from appearing as "recently used" when they haven't actually been used yet.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
