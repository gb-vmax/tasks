# Bug Report

### Describe the bug

The `isDefaultOrganizationProject` function is not correctly identifying default organization projects. Projects that should be recognized as default organization projects are being incorrectly filtered out.

### Reproduction

```js
// This should return true but returns false
const project1 = {
  remoteId: 'proj_org_12345'
};
isDefaultOrganizationProject(project1); // returns false, expected true

// This should also return true but returns false
const project2 = {
  remoteId: 'proj_team_67890'
};
isDefaultOrganizationProject(project2); // returns false, expected true
```

### Expected behavior

Both legacy projects with `proj_team_xxx` format and new projects with `proj_org_xxx` format should be identified as default organization projects. Currently, the function only returns `true` if a remoteId somehow contains BOTH prefixes, which is impossible in normal usage.

### System Info
- Insomnia version: latest
- OS: N/A (logic bug)

---
Repository: /testbed
