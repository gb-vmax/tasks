# Bug Report

### Describe the bug

After a recent update, the team schema is generating invalid IDs. The code appears to have syntax errors where function declarations are mixed with object properties, causing the application to fail at runtime.

### Reproduction

When trying to use the team schema to create or retrieve team data:

```js
import { teamSchema } from './type-schemas';

// Attempting to access the schema causes an error
const team = {
  id: teamSchema.id(),
  name: teamSchema.name()
};
```

The application crashes with a syntax error instead of generating the expected team object.

### Expected behavior

The `teamSchema` should be a valid object with callable properties that generate team IDs and names. Previously, it would return a simple 'teamId' string, but now the schema definition itself is malformed.

### System Info
- Node version: 18.x
- Package: insomnia/sync

The schema definition seems to have function declarations (`let`, `const`, `export`) inside what should be a plain object literal, which isn't valid JavaScript syntax.

---
Repository: /testbed
