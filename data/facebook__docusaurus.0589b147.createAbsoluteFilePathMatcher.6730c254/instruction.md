# Bug Report

### Describe the bug

I'm experiencing an issue with file path matching in `createAbsoluteFilePathMatcher`. When I have file paths that contain a folder name as part of their path (not at the root), the matcher is incorrectly treating them as if they belong to that folder.

### Reproduction

```js
const matcher = createAbsoluteFilePathMatcher(
  ['**/*.md'],
  ['/home/user/docs']
);

// This file path contains '/docs' in the middle but is not under /home/user/docs
const filePath = '/home/user/projects/docs/notes/file.md';

// The matcher incorrectly matches this file
matcher(filePath);
```

### Expected behavior

The file path matcher should only match files that are actually located under the specified root folders. Files that happen to contain the root folder name as a substring in their path (but are not actually under that root) should not match.

For example:
- `/home/user/docs/file.md` → should match (actually under the root folder)
- `/home/user/projects/docs/file.md` → should NOT match (just happens to contain 'docs' in the path)

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
