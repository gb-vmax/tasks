# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with markdown parsing when using attention markers (like `*` and `_` for emphasis). The parser seems to be returning empty arrays or undefined values where it should be returning the actual attention markers.

### Reproduction

```js
import { remark } from 'remark';

const markdown = '*italic text* and **bold text**';
const result = remark().parse(markdown);

// Expected: proper emphasis nodes in the AST
// Actual: attention markers are not being recognized correctly
console.log(result);
```

When trying to parse markdown with emphasis/strong markers, the output doesn't include the expected formatting nodes. It appears that the `attentionMarkers` construct is not being properly exported or is returning an empty array instead of the actual marker characters.

### Expected behavior

The parser should correctly recognize attention markers (`*`, `_`, etc.) and create appropriate emphasis/strong nodes in the AST. Previously this worked fine, but something changed that's causing the markers to not be detected.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
