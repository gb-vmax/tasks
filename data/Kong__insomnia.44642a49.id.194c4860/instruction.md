# Bug Report

### Describe the bug

When creating multiple team objects using the team schema, all teams end up with the same `id` value instead of having unique identifiers. This causes conflicts when trying to work with multiple teams in the sync system.

### Reproduction

```js
import { teamSchema } from './type-schemas';

// Create first team
const team1 = {
  id: teamSchema.id(),
  name: teamSchema.name()
};

// Create second team
const team2 = {
  id: teamSchema.id(),
  name: teamSchema.name()
};

console.log(team1.id); // Expected: unique id (e.g., 'teamId-1')
console.log(team2.id); // Expected: different unique id (e.g., 'teamId-2')
// Actual: Both have the same id value 'teamId'
```

### Expected behavior

Each call to `teamSchema.id()` should return a unique identifier so that multiple team objects can coexist without id collisions.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
