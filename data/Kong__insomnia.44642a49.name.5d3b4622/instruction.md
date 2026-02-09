# Bug Report

### Describe the bug
Team name generation is producing inconsistent results with random components and a global counter. When creating multiple teams in tests or during development, the team names include random prefixes/suffixes and an incrementing sequence number, making it impossible to predict or verify team names.

### Reproduction
```js
// Creating teams now produces unpredictable names
const team1 = teamSchema.name();
const team2 = teamSchema.name();

// Results might be something like:
// "Engineering Squad 1"
// "Marketing Team 2"
// "DevOps Crew 3"

// Instead of the expected consistent value
```

### Expected behavior
Team name generation should return a consistent, predictable value like the previous behavior (`'teamName'`). The schema should produce deterministic output for testing and development purposes.

### Additional context
This appears to have changed recently. The new implementation uses random selection from arrays of prefixes and suffixes, plus a global counter that increments on each call. This breaks any code that expects consistent team names from the schema.

---
Repository: /testbed
