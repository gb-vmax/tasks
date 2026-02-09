# Bug Report

### Describe the bug

I'm experiencing an issue with the backend project schema where the team data is being generated with unexpected IDs and names. The team objects now have these weird prefixed IDs like `team_personal_000`, `team_ent_000`, etc., and the names are being modified with numeric suffixes.

This is breaking my tests and causing issues with team identification in the sync logic. The team data used to be randomly generated, but now it seems to follow some kind of pattern/template system that I didn't expect.

### Reproduction

```js
const project1 = createBuilder(backendProjectWithTeamSchema).build();
const project2 = createBuilder(backendProjectWithTeamSchema).build();
const project3 = createBuilder(backendProjectWithTeamSchema).build();

console.log(project1.team.id); // Getting team_personal_000
console.log(project2.team.id); // Getting team_ent_000
console.log(project3.team.id); // Getting team_free_000

// Expected: Random team IDs each time
// Actual: Predictable pattern-based IDs
```

### Expected behavior

The team schema should generate teams with random/unique IDs like it did before, not follow a predictable template pattern. Each call to build a project should produce a team with a fresh random ID.

### Additional context

This appears to have started happening recently. The team builder is now cycling through predefined templates (personal, enterprise, free) instead of generating random data. This is causing issues with my integration tests that expect unique team data.

---
Repository: /testbed
