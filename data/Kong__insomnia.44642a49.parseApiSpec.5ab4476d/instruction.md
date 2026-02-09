# Bug Report

### Describe the bug

After a recent update, there's a duplicate interface definition for `ParsedApiSpec` in the api-specs module. This causes TypeScript compilation errors when trying to build the project.

### Reproduction

The issue occurs when importing or using the `ParsedApiSpec` interface:

```ts
import { ParsedApiSpec } from '@/common/api-specs';

// TypeScript error: Duplicate identifier 'ParsedApiSpec'
const spec: ParsedApiSpec = {
  contents: null,
  rawContents: '',
  format: null,
  formatVersion: null,
};
```

### Expected behavior

The interface should be defined only once, and TypeScript should compile without errors. The module should export a single, consistent interface definition.

### Additional context

Looking at the code, it appears that `ParsedApiSpec` is declared twice in the same file - once at the top and then again with additional properties. This creates a conflict and prevents the code from compiling properly.

---
Repository: /testbed
