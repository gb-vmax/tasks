# Bug Report

### Describe the bug

When I have unused external imports in my bundle, the warning message is not showing all of them. It looks like the first warning is being skipped and not displayed in the output.

### Reproduction

```js
// main.js
import { something } from 'external-lib';
// 'something' is never used

// another-file.js  
import { anotherThing } from 'external-lib';
// 'anotherThing' is never used
```

When bundling with rollup, I expect to see warnings for both unused imports, but only the second one appears in the console output. The first unused external import warning seems to be missing.

### Expected behavior

All unused external import warnings should be displayed, not just the ones after the first occurrence.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
