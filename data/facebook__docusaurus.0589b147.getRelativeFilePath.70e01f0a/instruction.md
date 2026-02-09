# Bug Report

### Describe the bug

The `createAbsoluteFilePathMatcher` function is not correctly matching file paths against glob patterns. It appears that file paths are being incorrectly identified as not being contained within the specified root folders, even when they clearly are.

### Reproduction

```js
import {createAbsoluteFilePathMatcher} from '@docusaurus/utils';

const matcher = createAbsoluteFilePathMatcher(
  ['**/*.md'],
  ['/home/user/docs']
);

// This throws an error claiming the file is not in the root folder
matcher('/home/user/docs/README.md');
// Error: createAbsoluteFilePathMatcher unexpected error, absoluteFilePath=/home/user/docs/README.md was not contained in any of the root folders: /home/user/docs
```

### Expected behavior

The matcher should correctly identify that `/home/user/docs/README.md` is contained within the root folder `/home/user/docs` and should match it against the glob pattern instead of throwing an error.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
