# Bug Report

### Describe the bug

After a recent update, the sync conflict resolution system appears to be broken. When attempting to merge branches with conflicts, the application throws an error about missing conflict handlers even though the conflicts should be resolvable.

### Reproduction

I'm experiencing this issue when trying to sync changes between branches. Here's what happens:

1. Make changes to the same resource in two different branches
2. Attempt to merge/pull changes
3. The sync process fails with an error about conflict handling

The sync operation used to work fine before, but now it seems like the conflict resolution flow is not working as expected. It looks like conflicts are being processed but then the handler is still being called incorrectly.

### Expected behavior

The sync should either:
- Auto-resolve conflicts when possible (e.g., when both sides have identical changes)
- Present remaining conflicts to the user through the conflict handler
- Complete successfully when all conflicts are resolved

Instead, it's throwing errors during the merge process even when conflicts should be handleable.

### System Info
- Insomnia version: latest
- OS: Multiple (reproduced on macOS and Windows)

This is blocking our team's workflow as we can't sync changes between branches anymore. Any help would be appreciated!

---
Repository: /testbed
