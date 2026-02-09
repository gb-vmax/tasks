# Bug Report

### Describe the bug

When using `export * from` with modules that have synthetic named exports, the re-export behavior is not working as expected. Specifically, when a module has a synthetic named export with the same name as a regular export being re-exported, the regular export is being incorrectly hidden instead of taking precedence.

### Reproduction

```js
// module-a.js
export const foo = 'regular export';

// module-b.js
export * from './module-a.js';
// This module has syntheticNamedExports = 'foo'

// main.js
import { foo } from './module-b.js';
console.log(foo); // Expected: 'regular export', but synthetic export is used instead
```

### Expected behavior

Regular exports should take precedence over synthetic named exports when both exist with the same name. The synthetic namespace should not hide "regular" exports of the same name during the `export *` resolution.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
