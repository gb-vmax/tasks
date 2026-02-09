# Bug Report

### Describe the bug

I'm encountering a syntax error in the schema definitions after a recent update. It looks like there's malformed code in the `branchSchema` object definition - there are function declarations appearing before the object properties which is causing JavaScript parsing errors.

### Reproduction

When trying to use the branch schema, I get a syntax error. The issue appears to be in the `type-schemas.ts` file where the `branchSchema` object is defined.

```js
// Attempting to use branchSchema results in:
// SyntaxError: Unexpected token 'const'

const schema = branchSchema;
// This fails to parse
```

### Expected behavior

The `branchSchema` should be a valid JavaScript object with properly defined properties. The schema should initialize without syntax errors and the `created` field should generate appropriate date values.

### System Info
- Package: @insomnia/sync
- Node version: 18.x

The code structure seems to have helper functions (`getDateGenerationMode`, `generateRecentDate`, `getSchemaDate`) defined inside the object literal itself, which isn't valid JavaScript syntax. These functions should probably be defined outside the object before being referenced.

---
Repository: /testbed
