# Bug Report

### Describe the bug

After a recent update, I'm experiencing an issue where merge conflict messages are displaying "String" instead of the actual message content. This appears to be affecting the sync functionality when conflicts are detected.

### Reproduction

When a merge conflict occurs during sync operations, the conflict message is not being displayed correctly. Instead of showing the expected message text, it's showing the constructor name.

Steps to reproduce:
1. Create a sync conflict scenario (e.g., modify the same resource on two different clients)
2. Trigger a sync operation
3. Check the merge conflict message property
4. The message shows "String" instead of the actual conflict message

### Expected behavior

The merge conflict should display a descriptive message like "message" to help users understand what conflict occurred. The message property should contain the actual string value, not a constructor reference.

### Additional context

This seems to have started appearing after changes to the merge conflict schema. The message field is critical for debugging sync conflicts and helping users resolve them properly.

---
Repository: /testbed
