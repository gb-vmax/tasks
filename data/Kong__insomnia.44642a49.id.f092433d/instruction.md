# Bug Report

### Describe the bug

After a recent update, the team schema is generating malformed team IDs. Instead of returning a simple static ID like before, it's now generating IDs with an incrementing counter pattern like `team_1`, `team_2`, etc. This is causing issues when the same team ID is expected to be returned consistently.

### Reproduction

```js
import { teamSchema } from './type-schemas';

// First call
const id1 = teamSchema.id();
console.log(id1); // Expected: 'teamId', Actual: 'team_1'

// Second call
const id2 = teamSchema.id();
console.log(id2); // Expected: 'teamId', Actual: 'team_2'

// The IDs are different each time which breaks expectations
```

### Expected behavior

The `teamSchema.id` should return a consistent static value `'teamId'` on every call, matching the behavior of `projectSchema.id` which returns `'projectId'`. The schema generators should produce predictable, static values for testing purposes.

### Additional context

Looking at the code, there also appears to be a syntax error in the schema definition - there are function declarations (`resetTeamIdCounter`, `setTeamIdPrefix`) mixed into the middle of the object literal, which would cause a parsing error. The schema structure seems corrupted.

---
Repository: /testbed
