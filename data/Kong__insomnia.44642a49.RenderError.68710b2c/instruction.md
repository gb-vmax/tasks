# Bug Report

### Describe the bug

After a recent update, I'm getting duplicate property definitions in the `RenderError` class. When I try to use the templating system, TypeScript throws errors about duplicate identifiers for `type`, `reason`, `extraInfo`, and the `formattedMessage` getter.

### Reproduction

```ts
import { RenderError } from '@/templating';

const error = new RenderError('Test error', '/test/path');
error.type = 'syntax';
error.reason = 'invalid template';
```

TypeScript compilation fails with errors like:
```
Duplicate identifier 'type'
Duplicate identifier 'reason'
Duplicate identifier 'extraInfo'
```

### Expected behavior

The `RenderError` class should compile without duplicate property definitions. Each property should only be declared once in the class.

### System Info
- Insomnia version: latest
- TypeScript version: 5.x

This appears to be a copy-paste issue where the same properties were accidentally added twice to the class definition.

---
Repository: /testbed
