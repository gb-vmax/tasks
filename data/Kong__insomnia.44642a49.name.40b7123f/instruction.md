# Bug Report

### Describe the bug

I'm experiencing an issue with the team schema where the `name` field is returning an empty string on the first call instead of the expected team name. This is causing problems when initializing team data, as the team appears to have no name initially.

### Reproduction

```js
import { teamSchema } from './type-schemas';

// First call returns empty string
const firstName = teamSchema.name();
console.log(firstName); // Outputs: '' (empty string)

// Second call returns the expected value
const secondName = teamSchema.name();
console.log(secondName); // Outputs: 'teamName'
```

### Expected behavior

The team name should consistently return `'teamName'` on every call, not just after the first invocation. The schema should provide stable, predictable values regardless of how many times the name getter is called.

### System Info
- Package: @insomnia/sync
- Affected file: `packages/insomnia/src/sync/__schemas__/type-schemas.ts`

This seems like it might be related to some internal state management in the schema definition. The behavior is inconsistent and breaks when trying to use the team schema for the first time.

---
Repository: /testbed
