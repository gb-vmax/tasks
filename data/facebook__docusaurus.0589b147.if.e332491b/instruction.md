# Bug Report

### Describe the bug

When trying to retrieve git commit history for a file, the function throws an error saying the file exists when it actually does exist. This is preventing me from getting file metadata like last modified dates and authors.

### Reproduction

```js
import {getFileCommitDate} from '@docusaurus/utils';

// Trying to get commit date for an existing file
const filePath = './docs/intro.md';
await getFileCommitDate(filePath);

// Error: Failed to retrieve git history for "./docs/intro.md" because the file exists.
```

The error message doesn't make sense - it's complaining that the file exists, but shouldn't it only work if the file exists?

### Expected behavior

The function should successfully return the commit date for existing files. It should only throw an error if the file doesn't exist, not when it does exist.

### System Info
- @docusaurus/utils version: latest
- Node.js: v18.x

---
Repository: /testbed
