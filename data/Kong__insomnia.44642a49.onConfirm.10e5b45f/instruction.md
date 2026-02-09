# Bug Report

### Describe the bug

When switching body types in the request editor, the confirmation dialog appears but clicking "Confirm" doesn't actually change the body type. The dialog closes but the body type remains unchanged and the body content is not updated.

### Reproduction

1. Open a request with a specific body type (e.g., JSON with some content)
2. Click on the Content-Type dropdown to switch to a different body type (e.g., Form URL Encoded)
3. Confirm the switch in the dialog that appears
4. Notice that the body type doesn't actually change

### Expected behavior

After confirming the body type switch, the request body should be updated to the new MIME type. The body content should be converted if possible (e.g., JSON object to form parameters), or cleared if conversion isn't possible.

### System Info

- Insomnia version: latest
- OS: macOS

The confirmation dialog shows up correctly and asks "Current body will be lost. Are you sure you want to continue?", but after clicking confirm nothing happens. This seems to have broken recently as it was working before.

---
Repository: /testbed
