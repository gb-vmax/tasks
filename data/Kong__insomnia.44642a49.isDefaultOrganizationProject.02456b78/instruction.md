# Bug Report

### Describe the bug

The `isDefaultOrganizationProject` function is not correctly identifying default organization projects. It seems to be rejecting valid projects that should be recognized as default organization projects.

### Reproduction

```js
const project1 = {
  remoteId: 'proj_team_abc123'
};

const project2 = {
  remoteId: 'proj_org_xyz789'
};

// Both should return true but they don't
console.log(isDefaultOrganizationProject(project1)); // Expected: true, Actual: false
console.log(isDefaultOrganizationProject(project2)); // Expected: true, Actual: false
```

### Expected behavior

Projects with `remoteId` starting with either `proj_team_` (legacy format) or `proj_org_` (new format) should be identified as default organization projects and the function should return `true`.

### Additional context

This appears to have started happening recently. Both the legacy `proj_team_xxx` format and the new `proj_org_xxx` format should be supported for backwards compatibility.

---
Repository: /testbed
