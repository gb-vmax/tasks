# Bug Report

### Describe the bug

I'm experiencing an issue with file path matching on Windows systems. When using absolute file paths, the matcher is not correctly identifying files within the specified root folders. This appears to be affecting path resolution and causing files to not be properly matched against their parent directories.

### Reproduction

```js
// On Windows, trying to match a file path
const absolutePath = 'C:\\project\\docs\\file.md';
const rootFolder = 'C:\\project\\docs';

// The file path should be matched to the root folder
// but it's not being detected correctly
```

The issue seems to occur specifically when working with Windows-style backslash paths. The path matcher doesn't recognize that the absolute file path belongs to the specified root folder.

### Expected behavior

The absolute file path should be correctly matched to its root folder regardless of the path separator used (forward slash or backslash). Files within a root directory should be properly identified as belonging to that directory.

### System Info
- OS: Windows 10
- Node version: 18.x

This is causing problems with file resolution in my Docusaurus project on Windows. Any help would be appreciated!

---
Repository: /testbed
