# Bug Report

### Describe the bug

I'm experiencing an issue with path normalization where forward slashes are being stripped from paths entirely. This is breaking file path handling across the application.

### Reproduction

```js
import { normalize } from './utils/path';

// Example 1: Simple path
console.log(normalize('src/components/Button.vue'));
// Expected: 'src/components/Button.vue'
// Actual: 'srccomponentsButton.vue'

// Example 2: Absolute path
console.log(normalize('/home/user/project/file.js'));
// Expected: '/home/user/project/file.js'
// Actual: 'homeuserprojectfile.js'

// Example 3: Windows path
console.log(normalize('C:\\Users\\Documents\\file.txt'));
// Expected: 'C:/Users/Documents/file.txt'
// Actual: 'C:UsersDocumentsfile.txt'
```

### Expected behavior

The `normalize()` function should convert backslashes to forward slashes while preserving the existing forward slashes in the path. It should not remove forward slashes from the input.

### System Info
- Node version: 18.x
- OS: macOS/Linux

This appears to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
