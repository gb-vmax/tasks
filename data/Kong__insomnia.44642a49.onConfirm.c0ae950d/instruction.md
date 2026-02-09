# Bug Report

### Describe the bug

When switching request body types in the UI, the content type dropdown is not working correctly. After attempting to change the body type, the application crashes or behaves unexpectedly.

### Reproduction

1. Open a request in Insomnia
2. Navigate to the body tab
3. Try to switch from one content type to another (e.g., from Form URL Encoded to JSON)
4. Confirm the dialog that asks if you want to switch body types

The application encounters an error when trying to process the body type change.

### Expected behavior

The body type should switch smoothly, and if there's a confirmation dialog, clicking "confirm" should complete the type change without errors. The request should update to use the new content type.

### System Info
- Insomnia version: latest
- OS: Windows/Mac/Linux

This seems to have started happening recently. The content type switching was working fine before.

---
Repository: /testbed
