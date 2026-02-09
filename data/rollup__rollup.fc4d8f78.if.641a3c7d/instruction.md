# Bug Report

### Describe the bug

I'm experiencing an issue with `export * from` statements when dealing with modules that have synthetic named exports. The behavior seems to have changed recently and exports are not being resolved correctly.

When a module re-exports everything from another module using `export * from './other'`, and that other module has `syntheticNamedExports` configured, the export resolution doesn't work as expected. Specifically, exports that should be available are being skipped or not found properly.

### Reproduction

```js
// module-a.js
export const foo = 'bar';

// module-b.js (with syntheticNamedExports: 'foo')
export const baz = 'qux';

// module-c.js
export * from './module-b';

// main.js
import { baz } from './module-c';
console.log(baz); // Expected to work but doesn't resolve correctly
```

The issue appears when trying to access named exports through a re-export chain where one of the modules in the chain has `syntheticNamedExports` set.

### Expected behavior

Named exports should be properly resolved through `export * from` statements even when intermediate modules have `syntheticNamedExports` configured. The export resolution logic should correctly handle these cases and make the exports available.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
