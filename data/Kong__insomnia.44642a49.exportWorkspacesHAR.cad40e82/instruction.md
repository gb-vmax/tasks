# Bug Report

### Describe the bug

When exporting multiple workspaces to HAR format, only the first workspace that completes is being exported instead of all workspaces. This results in incomplete HAR exports when working with multiple workspaces.

### Reproduction

```js
// Export multiple workspaces
const workspaces = [workspace1, workspace2, workspace3];
await exportWorkspacesHAR(workspaces, false);

// Expected: HAR file contains requests from all 3 workspaces
// Actual: HAR file only contains requests from whichever workspace finished loading first
```

### Steps to reproduce:
1. Create multiple workspaces with different requests
2. Attempt to export all workspaces to HAR format
3. Check the exported HAR file
4. Notice that only one workspace's requests are included

### Expected behavior

The HAR export should include requests from ALL selected workspaces, not just the first one that finishes processing.

### System Info
- Insomnia version: latest
- OS: Any

This is causing data loss when users try to export their entire workspace collection for backup or sharing purposes.

---
Repository: /testbed
