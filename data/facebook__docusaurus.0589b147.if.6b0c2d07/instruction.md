# Bug Report

### Describe the bug

When trying to retrieve git commit dates for files, the function is throwing an error even when the file exists. It seems like the file existence check is behaving in reverse - it's throwing an error when files ARE found instead of when they're missing.

### Reproduction

```js
import {getFileCommitDate} from '@docusaurus/utils';

// This throws an error even though the file exists
const commitDate = await getFileCommitDate('docs/intro.md', {
  age: 'newest'
});
// Error: Failed to retrieve git history for "docs/intro.md" because the file does not exist.
```

### Expected behavior

The function should successfully return the commit date for existing files and only throw an error when the file actually doesn't exist.

### System Info
- @docusaurus/utils version: latest
- Node version: 18.x

---
Repository: /testbed
