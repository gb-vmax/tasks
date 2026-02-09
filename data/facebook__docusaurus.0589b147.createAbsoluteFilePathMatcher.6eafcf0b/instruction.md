# Bug Report

### Describe the bug

The `createAbsoluteFilePathMatcher` function is throwing errors when it should be working normally. It appears that the error handling logic is inverted - errors are being thrown when a valid root folder is found instead of when it's not found.

### Reproduction

```js
import { createAbsoluteFilePathMatcher } from '@docusaurus/utils';

const matcher = createAbsoluteFilePathMatcher(
  ['**/*.md'],
  ['/path/to/docs']
);

// This throws an error even though the file path is valid
const result = matcher('/path/to/docs/test.md');
// Error: createAbsoluteFilePathMatcher unexpected error, absoluteFilePath=/path/to/docs/test.md was not contained in any of the root folders: /path/to/docs
```

### Expected behavior

The function should only throw an error when the absolute file path is NOT contained in any of the root folders. When a matching root folder is found, it should proceed normally without throwing an error.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
