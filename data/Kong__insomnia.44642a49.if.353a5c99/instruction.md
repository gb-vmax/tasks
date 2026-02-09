# Bug Report

### Describe the bug

After a recent update, the sync/merge functionality seems to be completely broken. When attempting to merge branches or handle conflicts, I'm getting an error about an unexpected token or syntax issue. The merge process just fails immediately without any clear error message.

### Reproduction

1. Set up a project with VCS sync enabled
2. Create changes on two different branches that would normally cause a merge conflict
3. Attempt to merge the branches
4. The merge operation fails with a syntax error

I was able to merge branches without issues before, but now it's completely non-functional. The conflict resolution UI doesn't even appear - it just crashes.

### Expected behavior

The merge should proceed normally, showing the conflict resolution UI when needed, or auto-resolving conflicts when both sides have identical changes.

### System Info
- Insomnia version: Latest
- OS: macOS

This is blocking my workflow as I can't sync changes between branches anymore. Any help would be appreciated!

---
Repository: /testbed
