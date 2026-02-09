# Bug Report

### Describe the bug

After a recent update, the API spec parser is now adding unexpected `warnings` property to the parsed result object. This breaks type checking and causes issues when trying to use the parsed spec since the `ParsedApiSpec` interface doesn't include a `warnings` field.

### Reproduction

```ts
import { parseApiSpec } from './api-specs';

const yamlSpec = `
openapi: 3.0.0
info:
  title: My API
  version: 1.0.0
paths: {}
`;

const result = parseApiSpec(yamlSpec);

// TypeScript error: Property 'warnings' does not exist on type 'ParsedApiSpec'
if (result.warnings) {
  console.log(result.warnings);
}

// Also breaks when destructuring
const { format, formatVersion, contents, warnings } = result;
// Error: Property 'warnings' does not exist on type 'ParsedApiSpec'
```

The parser is now attaching a `warnings` array to the result object using `(result as any).warnings = warnings;`, but the `ParsedApiSpec` interface only defines three properties: `contents`, `format`, and `formatVersion`.

### Expected behavior

Either:
1. The `warnings` property should be included in the `ParsedApiSpec` interface definition, or
2. The warnings shouldn't be added to the result object at all

The current implementation breaks type safety and causes runtime issues when code expects the result to match the defined interface.

### System Info
- TypeScript version: 4.x+
- Package: insomnia

---
Repository: /testbed
