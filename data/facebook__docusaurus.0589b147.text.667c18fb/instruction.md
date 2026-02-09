# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the remark library. The JavaScript bundle appears to be malformed and won't load properly.

### Reproduction

```js
import { remark } from 'remark';

const processor = remark();
// SyntaxError: Unexpected token ')'
```

The error occurs immediately when trying to import or use any functionality from remark. Looking at the bundled code, there seems to be a syntax issue in the exports section.

### Expected behavior

The library should import and initialize without any syntax errors. The processor should be created successfully.

### System Info
- remark version: 15.0.1
- Node version: 18.x
- Browser: N/A (build fails)

---
Repository: /testbed
