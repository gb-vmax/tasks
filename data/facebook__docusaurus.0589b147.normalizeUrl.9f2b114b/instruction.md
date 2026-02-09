# Bug Report

### Describe the bug

When using `normalizeUrl()` with file protocol URLs, the function incorrectly handles URLs that have exactly two slashes after `file:` (e.g., `file://path`). The current implementation only checks for three slashes (`file:///`) but should also handle the two-slash case.

### Reproduction

```js
import { normalizeUrl } from '@docusaurus/utils';

// This doesn't work correctly
const result = normalizeUrl(['file://some/path', 'to/file.txt']);
console.log(result);
// Expected: file:///some/path/to/file.txt
// Actual: incorrect normalization
```

The issue occurs when the file URL starts with `file://` (two slashes) instead of `file:///` (three slashes). The regex pattern `^file:\/\/\/` doesn't match the two-slash variant, causing the URL to be normalized incorrectly.

### Expected behavior

Both `file://` and `file:///` should be properly recognized and normalized to `file:///` in the output.

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
