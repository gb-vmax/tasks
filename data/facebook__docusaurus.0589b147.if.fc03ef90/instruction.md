# Bug Report

### Describe the bug

When trying to retrieve git commit history for a file using `getFileCommitDate()`, the function throws an error saying the file doesn't exist even when the file is actually present in the repository.

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

The function should successfully retrieve the git commit date for existing files. It should only throw the "file does not exist" error when the file actually doesn't exist.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. The error message is misleading since the file is definitely there.

---
Repository: /testbed
