# Bug Report

### Describe the bug

After a recent update, the request group duplication functionality appears to be broken. When trying to duplicate a folder in the workspace, the operation fails to complete and the duplicate folder doesn't appear.

### Reproduction

1. Create a new folder/request group in your workspace
2. Add some nested folders or requests inside it
3. Try to duplicate the folder
4. The duplication process seems to hang or fail silently

This was working fine before but now duplicating folders doesn't seem to work at all. The original folder remains but no copy is created.

### Expected behavior

When duplicating a request group/folder, a new copy should be created with a name like "Folder Name (Copy)" or "Folder Name (Copy 2)" if there are already duplicates. All nested items should also be duplicated recursively.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
