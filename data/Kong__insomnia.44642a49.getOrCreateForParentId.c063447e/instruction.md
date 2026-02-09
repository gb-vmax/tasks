# Bug Report

### Describe the bug

I'm experiencing an issue with cookie jar creation in the app. When working with multiple workspaces or switching between them, I'm seeing duplicate cookie jars being created instead of reusing the existing one. This is causing cookies to not persist correctly across sessions.

### Reproduction

1. Create a new workspace
2. Make a request that sets cookies
3. Close and reopen the workspace
4. Notice that a new cookie jar gets created instead of using the existing one
5. Previous cookies are lost

It seems like the system is creating a new cookie jar every time even when one already exists for the parent workspace.

### Expected behavior

The application should reuse the existing cookie jar for a workspace instead of creating duplicates. Only one cookie jar should exist per workspace, and it should be retrieved consistently using the same ID.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
