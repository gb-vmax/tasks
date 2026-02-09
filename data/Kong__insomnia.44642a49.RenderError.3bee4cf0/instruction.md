# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the templating engine. It looks like there's a problem with the `RenderError` class definition - the code appears to have duplicate property declarations which causes compilation to fail.

### Reproduction

When trying to import or use the templating module:

```ts
import { RenderError } from './templating';

// Attempting to create or use RenderError results in compilation errors
const error = new RenderError();
```

The TypeScript compiler throws errors about duplicate identifiers for `type`, `reason`, and `extraInfo` properties in the `RenderError` class.

### Expected behavior

The `RenderError` class should compile without errors and allow normal instantiation and usage. Properties should only be declared once in the class definition.

### System Info
- Insomnia version: latest
- Node version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
