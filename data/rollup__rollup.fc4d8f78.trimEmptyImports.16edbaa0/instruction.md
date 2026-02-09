# Bug Report

### Describe the bug

I'm experiencing an issue with empty import statements not being properly removed from the output bundle. It seems like imports without any actual imports or reexports are being kept in the final bundle instead of being trimmed away.

### Reproduction

```js
// input.js
import 'side-effects-module';
import {} from 'empty-module';
import { something } from 'actual-module';

export { something };
```

When bundling this code, the empty import from 'empty-module' remains in the output even though it has no imports or reexports. This bloats the bundle with unnecessary import statements.

### Expected behavior

Empty imports (those with no actual imports or reexports) should be removed from the final bundle output to keep the bundle clean and minimal. Only imports with side effects or actual imports/reexports should remain.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
