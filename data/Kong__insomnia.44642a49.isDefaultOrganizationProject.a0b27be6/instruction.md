# Bug Report

### Describe the bug

The `isDefaultOrganizationProject` function is not correctly identifying default organization projects. It seems like projects with legacy `proj_team_xxx` remote IDs are no longer being recognized as default organization projects.

### Reproduction

```js
const legacyProject = {
  remoteId: 'proj_team_12345'
};

const newProject = {
  remoteId: 'proj_org_67890'
};

// This returns false but should return true
isDefaultOrganizationProject(legacyProject);

// This also returns false 
isDefaultOrganizationProject(newProject);
```

### Expected behavior

Both legacy projects (with `proj_team_xxx` format) and new projects (with `proj_org_xxx` format) should be recognized as default organization projects and the function should return `true`.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
