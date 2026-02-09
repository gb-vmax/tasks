# Bug Report

### Describe the bug

I'm experiencing an issue with the `backendProjectWithTeamSchema` where the `team` property appears to be returning cached values instead of generating fresh team objects. When I try to create multiple backend projects with different team configurations, they end up sharing the same team instance.

### Reproduction

```js
const project1 = createBuilder(backendProjectWithTeamSchema)
  .team({ id: 'team-1', name: 'Team Alpha' })
  .build();

const project2 = createBuilder(backendProjectWithTeamSchema)
  .team({ id: 'team-2', name: 'Team Beta' })
  .build();

// Both projects have the same team reference
console.log(project1.team === project2.team); // Expected: false, Actual: true
console.log(project1.team.id); // Expected: 'team-1', but might get cached value
```

### Expected behavior

Each call to build a backend project with team should create independent team objects. Different projects should have different team instances, especially when different overrides are provided.

### Additional context

This seems to have started after some recent changes to the schema definitions. The team objects are being reused across different project instances which causes problems when trying to create multiple projects with distinct teams.

---
Repository: /testbed
