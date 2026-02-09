# Bug Report

### Describe the bug

The `status()` method in GitVCS is not returning the correct type when called with an array of filepaths. When passing multiple files to check their git status, the method returns a `Map<string, string>` instead of a single status string, which breaks existing code that expects a string return value.

### Reproduction

```js
const gitVcs = new GitVCS();

// Single file - works as expected
const singleStatus = await gitVcs.status('path/to/file.txt');
console.log(typeof singleStatus); // 'string'

// Multiple files - returns Map instead of string
const multiStatus = await gitVcs.status(['path/to/file1.txt', 'path/to/file2.txt']);
console.log(typeof multiStatus); // 'object' (Map)

// This causes issues when code expects a string
if (multiStatus === 'modified') { // This comparison fails
  // Never executes
}
```

### Expected behavior

The method signature changed to accept `string | string[]` but the return type is inconsistent. When an array is passed, it returns a Map, but existing code that calls this method expects a string return value. This causes type errors and runtime issues in code that was working before.

Either the return type should be consistent, or there should be a separate method for batch status checks to avoid breaking existing functionality.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
