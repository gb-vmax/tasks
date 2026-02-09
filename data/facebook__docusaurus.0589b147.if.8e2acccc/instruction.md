# Bug Report

### Describe the bug

I'm getting an error when trying to retrieve git commit dates for files, even though git is properly installed on my system. The function throws an error saying "git is not installed" when git is clearly available and working.

### Reproduction

```js
import { getFileCommitDate } from '@docusaurus/utils';

// This throws an error even when git is installed
const commitDate = await getFileCommitDate({
  file: './docs/intro.md',
  age: 'oldest'
});
```

### Expected behavior

The function should successfully retrieve the git commit date when git is installed and available in the system PATH. It should only throw the "git is not installed" error when git is actually missing.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS/Linux

Has anyone else encountered this? It's blocking my build process since it fails immediately when trying to get file history.

---
Repository: /testbed
