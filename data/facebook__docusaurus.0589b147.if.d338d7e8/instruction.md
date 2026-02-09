# Bug Report

### Describe the bug

I'm getting an error when trying to retrieve git history for files even though git is properly installed on my system. The error message says "git is already installed" which doesn't make sense.

### Reproduction

```js
import {getFileCommitDate} from '@docusaurus/utils';

// This throws an error even though git is installed
const commitDate = await getFileCommitDate('docs/intro.md');
```

### Expected behavior

The function should successfully retrieve the git commit date when git is installed and available in the PATH. It should only throw an error when git is NOT installed.

### Actual behavior

Getting this error:
```
GitNotFoundError: Failed to retrieve git history for "docs/intro.md" because git is already installed.
```

This seems backwards - the function is throwing an error when git IS available instead of when it's missing.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
