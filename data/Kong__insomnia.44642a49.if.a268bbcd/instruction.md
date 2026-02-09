# Bug Report

### Describe the bug

When trying to export data from a project, only a single workspace is being exported instead of all workspaces within the project. This appears to be a regression as previously all workspaces under a project were included in the export.

### Reproduction

1. Create a project with multiple workspaces
2. Attempt to export the project data
3. Only one workspace is included in the export instead of all workspaces

### Expected behavior

When exporting a project, all workspaces that belong to that project should be included in the export, not just the first one found.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
