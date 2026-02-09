# Bug Report

### Describe the bug

The export type selection modal is broken - when I try to select an export format and click save, nothing happens. The modal just hangs and doesn't close or show any feedback.

### Reproduction

1. Open the export dialog
2. Try to select any export format (either built-in or custom)
3. Click the save/submit button
4. The modal doesn't respond and gets stuck

It seems like the callback that's supposed to handle the format selection isn't being called properly. I checked the console and there are no errors, but the export process never completes.

### Expected behavior

After selecting an export format and clicking save, the modal should close and the export should proceed (or show an error if something went wrong). The user should get some kind of feedback about what's happening.

### Additional context

This was working fine before, but now it's completely broken. I can't export anything because the format selection step never completes. Not sure if this is related to a recent update but it's blocking my workflow.

---
Repository: /testbed
