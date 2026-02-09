# Bug Report

### Describe the bug

After a recent update, all gRPC requests are showing as pinned by default when they shouldn't be. Additionally, the `lastActive` timestamp appears to be set to an invalid value (-1) instead of 0.

### Reproduction

1. Create a new gRPC request
2. Check the request metadata
3. The request is automatically pinned even though it should start unpinned
4. The `lastActive` field shows -1 instead of the expected 0

### Expected behavior

New gRPC requests should:
- Start with `pinned: false` (not pinned by default)
- Have `lastActive: 0` as the initial timestamp value

This is affecting the UI as all new requests appear in the pinned section immediately, which is not the intended behavior.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
