# Bug Report

### Describe the bug

I'm encountering an issue where exported variables are being included incorrectly in the output. It seems like variables that shouldn't be exported are being added to the export list, causing unexpected behavior in the bundled code.

### Reproduction

```js
// module1.js
const internalVar = 'internal';
export const publicVar = 'public';

// module2.js
import { publicVar } from './module1.js';
console.log(publicVar);
```

When bundling this code, `internalVar` appears to be included in the variables list even though it's not exported. This is causing issues with tree-shaking and creating larger bundle sizes than expected.

### Expected behavior

Only variables that are actually exported (like `publicVar`) should be included in the exported variables list. Internal/private variables that aren't exported should not be added.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
