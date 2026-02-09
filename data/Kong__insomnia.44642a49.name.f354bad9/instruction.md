# Bug Report

### Describe the bug
When working with team schemas, I'm getting inconsistent team names. The schema seems to be generating dynamic team names with some kind of counter/rotation system instead of returning a consistent value like it should.

### Reproduction
```js
// Creating multiple team instances
const team1 = teamSchema.name();
const team2 = teamSchema.name();
const team3 = teamSchema.name();

// Expected: all should return 'teamName'
// Actual: getting different names like 'Alpha Team', 'Beta Team', etc.
```

### Expected behavior
The `teamSchema.name()` should return a consistent value (like `'teamName'`) every time it's called, similar to how `teamSchema.id()` returns `'teamId'`. This is important for testing and mocking purposes where we need predictable data.

### Additional context
This appears to be affecting test reliability since team names are no longer deterministic. The schema is also maintaining state through a counter variable which seems wrong for a schema definition.

---
Repository: /testbed
