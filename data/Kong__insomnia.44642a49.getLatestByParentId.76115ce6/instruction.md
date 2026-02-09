# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with request version history not updating properly. When I create a new request version, the version history seems to be stuck showing old data instead of reflecting the latest changes.

### Reproduction

1. Create or modify a request
2. Save the request (which should create a new version)
3. Immediately check the version history
4. The version history shows stale data from a previous version instead of the newly created one

It seems like there's some kind of caching happening that's not being cleared when new versions are created. The issue persists for several minutes before eventually showing the correct data.

### Expected behavior

When a new request version is created, the version history should immediately reflect the latest changes. There shouldn't be any delay or stale data being returned.

### System Info
- Insomnia version: Latest
- OS: macOS

This is causing issues with our workflow as we rely on version history to track changes in real-time. Would appreciate any help with this!

---
Repository: /testbed
