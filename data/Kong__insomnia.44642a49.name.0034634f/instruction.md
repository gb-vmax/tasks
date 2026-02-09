# Bug Report

### Describe the bug
When syncing projects from the backend, the project name is not being populated correctly. All projects are showing up with empty names instead of their actual names.

### Reproduction
1. Sync a project from the backend
2. Check the project name in the UI
3. The name field is empty/blank instead of showing the actual project name

This seems to affect all synced projects. The `rootDocumentId` and `id` fields are working fine, but specifically the `name` field is coming through as an empty string.

### Expected behavior
The project name should be populated with the actual name from the backend project data, not an empty string.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
