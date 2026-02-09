# Bug Report

### Describe the bug

I'm encountering an issue with `getFileCommitDate()` where it doesn't properly validate file existence before attempting to retrieve git history. When passing a path to a file that doesn't exist, the function proceeds without throwing an error, which leads to unexpected behavior downstream.

### Reproduction

```js
import {getFileCommitDate} from '@docusaurus/utils';

// Pass a non-existent file path
const result = await getFileCommitDate(
  '/path/to/nonexistent/file.md',
  {age: 'oldest'}
);

// Expected: Error thrown
// Actual: No error, function continues execution
```

### Expected behavior

The function should throw an error with a clear message when the specified file doesn't exist, similar to how it validates other conditions (like checking if git is available).

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
