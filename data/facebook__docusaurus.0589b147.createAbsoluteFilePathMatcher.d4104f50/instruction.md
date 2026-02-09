# Bug Report

### Describe the bug

I'm experiencing an issue with file path matching where absolute file paths are not being correctly matched against their root folders. The matcher is throwing errors saying that file paths are not contained in any root folders, even when they clearly should be.

### Reproduction

```js
import {createAbsoluteFilePathMatcher} from '@docusaurus/utils';

const matcher = createAbsoluteFilePathMatcher(
  ['**/*.md'],
  ['/home/user/project/docs', '/home/user/project/blog']
);

// This throws an error unexpectedly
matcher('/home/user/project/docs/intro.md');
// Error: createAbsoluteFilePathMatcher unexpected error, absoluteFilePath=/home/user/project/docs/intro.md was not contained in any of the root folders...
```

### Expected behavior

The file path `/home/user/project/docs/intro.md` should be recognized as being within the `/home/user/project/docs` root folder and the matcher should work correctly without throwing errors.

### System Info
- @docusaurus/utils version: latest
- OS: Linux/macOS

This is blocking my build process as it's preventing files from being properly matched. Any help would be appreciated!

---
Repository: /testbed
