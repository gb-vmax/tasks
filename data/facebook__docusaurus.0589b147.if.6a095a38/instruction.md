# Bug Report

### Describe the bug

After a recent update, I'm getting an error when trying to retrieve git commit dates for files, even though git is installed and working correctly on my system. The error message says "git is not installed" but when I check `git --version` in my terminal, it works fine.

### Reproduction

```js
import {getFileCommitDate} from '@docusaurus/utils';

// This throws an error even though git is installed
const commitDate = await getFileCommitDate('path/to/file.md');
```

The error thrown is:
```
GitNotFoundError: Failed to retrieve git history for "path/to/file.md" because git is not installed.
```

### Expected behavior

The function should successfully retrieve the git commit date when git is installed on the system. It should only throw the "git is not installed" error when git is actually not available.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS / Linux
- Git is installed and accessible via command line

---
Repository: /testbed
