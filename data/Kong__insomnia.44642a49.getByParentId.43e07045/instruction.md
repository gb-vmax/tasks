# Bug Report

### Describe the bug

After a recent update, workspace metadata seems to not reflect changes immediately. When I update workspace settings or properties, the changes don't appear to take effect until I restart the application or switch to a different workspace and back.

### Reproduction

1. Open a workspace
2. Update workspace metadata (e.g., change active environment, update sidebar filters, or modify any workspace-specific settings)
3. Navigate to another workspace
4. Come back to the original workspace
5. The changes made in step 2 are not reflected - old values are shown instead

This seems to happen consistently when switching between workspaces. The metadata updates appear to be saved (they persist after restart) but the UI shows stale data when navigating between workspaces in the same session.

### Expected behavior

When workspace metadata is updated, the changes should be immediately visible and reflected in the UI, even when switching between different workspaces.

### Additional context

This wasn't happening in the previous version I was using. The issue seems to be related to how workspace metadata is being loaded/retrieved when switching between workspaces.

---
Repository: /testbed
