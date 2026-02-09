# Bug Report

### Describe the bug

I'm encountering a duplicate property definition issue in the `RenderError` class. When instantiating a `RenderError`, it appears that some properties are being defined twice, which causes unexpected behavior and potential conflicts.

### Reproduction

```ts
import { RenderError } from './templating/index';

// Create a RenderError instance
const error = new RenderError('Template rendering failed');

// Properties like type, reason, extraInfo appear to be defined multiple times
console.log(Object.getOwnPropertyNames(error));
```

### Expected behavior

Each property should only be defined once in the class. The `type`, `reason`, `extraInfo`, `originalStack`, and `templateSnippet` properties should have a single definition without duplication.

### Additional context

This seems to have been introduced recently. The class structure looks like it has duplicate property declarations which could lead to issues with property initialization and TypeScript compilation warnings.

---
Repository: /testbed
