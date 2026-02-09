# Bug Report

### Describe the bug

I'm experiencing an issue with team ID generation in the sync schemas. It looks like the code has a syntax error that's preventing the application from running properly. When trying to use any functionality related to team schemas, I get a JavaScript parsing error.

### Reproduction

The error occurs when the schema is loaded/imported:

```js
import { teamSchema } from './sync/__schemas__/type-schemas';

// This throws a syntax error before any code can execute
console.log(teamSchema);
```

### Expected behavior

The team schema should be properly defined and usable without throwing syntax errors. The `id` field should be a valid function that generates team IDs.

### System Info
- Node version: 18.x
- Package: @insomnia/insomnia

The application was working fine before, but after a recent update it's now failing to start due to this parsing issue in the type schemas file.

---
Repository: /testbed
