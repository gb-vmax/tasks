# Bug Report

### Describe the bug

After a recent update, I'm getting errors when trying to access workspace metadata. The application throws an error saying the parent workspace doesn't exist, even though I'm just trying to open an existing workspace.

### Reproduction

Steps to reproduce:
1. Open a workspace that was working fine before
2. The app throws an error: `Cannot create WorkspaceMeta: parent workspace [id] does not exist`
3. The workspace becomes inaccessible

This seems to happen inconsistently - sometimes the workspace opens fine, other times it fails. I noticed it might be related to timing, as it seems more likely to fail when opening the app for the first time or after switching between workspaces quickly.

### Expected behavior

The workspace should open normally without throwing errors about missing parent workspaces. If the workspace exists and was accessible before, its metadata should be retrievable.

### Additional context

This started happening after the latest update. Previously, workspaces would open without any issues. Now I'm seeing this error intermittently, and it's blocking me from accessing my work.

The error message mentions that it "Cannot create WorkspaceMeta" but I'm not trying to create anything new - just opening an existing workspace that has been there for weeks.

---
Repository: /testbed
