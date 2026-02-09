# Bug Report

### Describe the bug

The `isDefaultOrganizationProject` function is incorrectly identifying projects as default organization projects. It seems to be matching projects that shouldn't be considered default organization projects, and potentially missing some that should be matched.

### Reproduction

```js
const project1 = { remoteId: 'proj_team_abc123' };
const project2 = { remoteId: 'proj_org_xyz789' };
const project3 = { remoteId: 'proj_team' };

// Expected: true, but returns false
console.log(isDefaultOrganizationProject(project1));

// Expected: true, but returns false  
console.log(isDefaultOrganizationProject(project2));

// Expected: false (or maybe true?), but behavior is inconsistent
console.log(isDefaultOrganizationProject(project3));
```

### Expected behavior

Projects with `remoteId` starting with `proj_team_` (legacy format) or `proj_org_` (new format) should be correctly identified as default organization projects. The function should use proper prefix matching for both formats.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
