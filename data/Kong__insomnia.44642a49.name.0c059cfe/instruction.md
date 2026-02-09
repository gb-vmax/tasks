# Bug Report

### Describe the bug

After a recent update, I'm seeing syntax errors when trying to use the sync functionality. It looks like there's an issue with the team schema definition that's preventing the code from running properly.

### Reproduction

When trying to use any sync-related features that involve team schemas, the application fails to load or throws a syntax error. This appears to be affecting the entire sync module.

```js
// Attempting to use team schema results in errors
import { teamSchema } from './sync/__schemas__/type-schemas';

// Code fails to execute
const team = teamSchema.name();
```

### Expected behavior

The team schema should be properly defined and usable without syntax errors. The `name` property should be accessible and return a valid team name.

### Additional context

This seems to have broken after the latest changes to the type schemas. The sync module is completely unusable in its current state.

---
Repository: /testbed
