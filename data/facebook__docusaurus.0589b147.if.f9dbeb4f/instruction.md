# Bug Report

### Describe the bug

I'm encountering an issue with `getFileCommitDate()` where it's failing to retrieve git history for regular files. The function seems to be checking for the wrong file type and throwing an error with a confusing message.

### Reproduction

```js
import {getFileCommitDate} from '@docusaurus/utils';

// Try to get commit date for a regular file
const result = await getFileCommitDate('docs/intro.md', {
  age: 'newest',
});
```

### Expected behavior

The function should successfully retrieve the git commit date for the file `docs/intro.md`. Instead, it's throwing an error saying the file exists (which doesn't make sense as an error condition).

### Additional context

This seems to affect any regular file I try to pass to the function. The error message itself is also confusing - it says "because the file exists" which sounds like the opposite of what should be an error condition.

---
Repository: /testbed
