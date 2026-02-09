# Bug Report

### Describe the bug

I'm encountering a syntax error in the branch schema definition that's preventing the application from building. It looks like there's a malformed object structure in the `branchSchema` definition - there's a `let` statement appearing in the middle of an object literal which is causing parsing issues.

### Reproduction

The error occurs when trying to import or use the type schemas module:

```js
import { branchSchema } from './sync/__schemas__/type-schemas';

// Application fails to load due to syntax error in the schema definition
```

### Expected behavior

The `branchSchema` should be a valid object literal that can be properly parsed and used throughout the application. The schema definition should follow proper JavaScript object syntax without variable declarations appearing between properties.

### System Info
- Node version: 18.x
- Package: @insomnia/insomnia

The build process fails immediately when trying to compile this file. This appears to have been introduced in a recent change to the branch name generation logic.

---
Repository: /testbed
