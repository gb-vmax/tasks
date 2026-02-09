# Bug Report

### Describe the bug

After upgrading, I'm seeing duplicate client certificates being created in my workspace. When I open a workspace that already has certificates configured, the migration logic seems to be running again and creating additional copies of the same certificates.

### Reproduction

1. Create a workspace with client certificates already configured
2. Close and reopen the workspace
3. The certificates get duplicated each time the workspace is loaded

It looks like the migration from the old `certificates` array format to the new `clientCertificate` model is running multiple times instead of just once.

### Expected behavior

The migration should only run once per workspace. If certificates have already been migrated to the new format, they shouldn't be created again on subsequent workspace loads.

### Additional context

This is causing issues because:
- Multiple identical certificates are showing up in the UI
- The certificate list keeps growing every time I restart the app
- I have to manually delete the duplicates

The migration logic should probably check if certificates have already been migrated before attempting to migrate them again.

---
Repository: /testbed
