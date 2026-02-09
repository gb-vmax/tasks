# Bug Report

### Describe the bug

I'm experiencing an issue where import attributes warnings are being logged even when the attributes are identical between imports. It seems like the warning for inconsistent import attributes is being triggered incorrectly.

### Reproduction

```js
// file1.js
import data from './external.json' with { type: 'json' };

// file2.js  
import data from './external.json' with { type: 'json' };
```

When both files import the same external module with the exact same attributes, I'm getting warnings about inconsistent import attributes even though they're completely consistent.

### Expected behavior

No warning should be logged when the import attributes are the same across different imports of the same module. The warning should only appear when attributes actually differ between imports.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
