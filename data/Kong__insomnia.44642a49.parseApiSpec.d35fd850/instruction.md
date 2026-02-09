# Bug Report

### Describe the bug

After a recent update, the API spec parser is not working correctly. When parsing OpenAPI/Swagger documents, the parser seems to be returning an object with duplicate or conflicting type definitions, which causes TypeScript compilation errors in my project.

### Reproduction

```typescript
import { parseApiSpec } from '@insomnia/common/api-specs';

const openApiDoc = `
openapi: 3.0.0
info:
  title: My API
  version: 1.0.0
paths: {}
`;

const result = parseApiSpec(openApiDoc);
// TypeScript complains about the return type
console.log(result);
```

When trying to use the `parseApiSpec` function, I'm getting TypeScript errors about the return type. It seems like the `ParsedApiSpec` interface might be defined multiple times or has conflicting definitions.

### Expected behavior

The function should return a properly typed result without TypeScript compilation errors. The interface should be defined once with a clear structure.

### System Info
- Package: @insomnia/insomnia
- TypeScript version: 4.x+

This is blocking my ability to parse API specifications in my application. Any help would be appreciated!

---
Repository: /testbed
