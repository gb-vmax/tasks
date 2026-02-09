# Bug Report

### Describe the bug

After a recent update, I'm getting duplicate property declarations in the `RenderError` class. When trying to use the error handling in templating, TypeScript is throwing compilation errors about duplicate identifiers.

### Reproduction

```ts
import { RenderError } from './templating';

try {
  // Some templating operation
  throw new RenderError('Test error');
} catch (error) {
  if (error instanceof RenderError) {
    console.log(error.type);
    console.log(error.reason);
  }
}
```

The code fails to compile with errors like:
- Duplicate identifier 'type'
- Duplicate identifier 'reason'
- Duplicate identifier 'extraInfo'

### Expected behavior

The `RenderError` class should have a single declaration for each property and compile without errors. The class should properly extend Error and allow access to all its properties.

### System Info
- TypeScript version: 4.x+
- Package: insomnia/templating

---
Repository: /testbed
