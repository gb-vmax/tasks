# Bug Report

### Describe the bug

I'm experiencing an issue with the sync schema generation where the `statusCandidateSchema` appears to have a syntax error. When trying to use this schema, I'm getting unexpected behavior that suggests the object structure is malformed.

### Reproduction

When attempting to create a status candidate using the schema:

```js
import { statusCandidateSchema } from './type-schemas';

// Trying to use the schema
const candidate = {
  key: statusCandidateSchema.key(),
  name: statusCandidateSchema.name(),
  document: statusCandidateSchema.document()
};
```

The application fails to parse or execute properly. It seems like there's a problem with how the schema object is defined.

### Expected behavior

The `statusCandidateSchema` should be a valid object with properly defined properties that can be accessed and called as functions. The schema should generate appropriate values for `key`, `name`, and `document` fields.

### System Info
- Package: @insomnia/sync
- Node version: 18.x

---
Repository: /testbed
