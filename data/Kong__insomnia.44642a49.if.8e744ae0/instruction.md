# Bug Report

### Describe the bug

After a recent update, the sync functionality seems broken. When I try to sync my workspace, nothing happens and the state map appears to be empty even though there's data in the snapshot.

### Reproduction

I noticed this when trying to sync changes:

1. Make changes to a workspace/collection
2. Attempt to sync
3. The sync completes but no changes are actually synced
4. Checking the snapshot state map shows it's empty `{}`

It looks like the snapshot data is there (I can see it in the logs), but it's not being processed into the state map correctly. This is blocking my ability to sync any changes.

### Expected behavior

The snapshot state should be converted into a proper state map so that sync operations work as expected. Previously this was working fine before the recent changes.

### System Info
- Insomnia version: latest
- OS: macOS

This is pretty urgent as I can't sync any of my work right now. Any help would be appreciated!

---
Repository: /testbed
