# Bug Report

### Describe the bug

The `sanitizeFileName` function is incorrectly handling file names on Windows systems. When sanitizing file names that contain a drive letter (like `C:\foo`), the function is cutting off characters incorrectly, resulting in malformed file paths.

### Reproduction

```js
import { sanitizeFileName } from './utils/sanitizeFileName';

// Test with Windows path containing drive letter
const result = sanitizeFileName('C:\\Users\\test\\file.txt');
console.log(result);
// Expected: C:\_Users_test_file.txt
// Actual: C:Users_test_file.txt (missing backslash after drive letter)

// Test with longer drive letter path
const result2 = sanitizeFileName('D:\\projects\\myapp\\data.json');
console.log(result2);
// Expected: D:_projects_myapp_data.json
// Actual: D:projects_myapp_data.json
```

### Expected behavior

The function should preserve the drive letter correctly and replace only the invalid characters with underscores. The character immediately after the drive letter should be processed according to the invalid character rules, not blindly skipped.

### System Info
- OS: Windows 10
- Node version: 18.x

---
Repository: /testbed
