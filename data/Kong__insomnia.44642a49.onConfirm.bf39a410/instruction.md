# Bug Report

### Describe the bug

When switching between body types in the request editor, the confirmation dialog appears to be broken. After clicking confirm to switch body types, nothing happens and the body type doesn't actually change.

### Reproduction

1. Create a new request with a JSON body
2. Add some JSON content to the body
3. Try to switch the body type to XML using the content-type dropdown
4. Click "Confirm" on the dialog that asks "Current body will be lost. Are you sure you want to continue?"
5. The dialog closes but the body type remains as JSON

### Expected behavior

The body type should change to the selected type (e.g., XML) after confirming the dialog. If there's content migration logic, it should convert the body content appropriately.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like it might be related to the confirmation dialog callback not being properly set up. The dialog appears but doesn't execute the action.

---
Repository: /testbed
