# Bug Report

### Describe the bug

I'm encountering an issue with file path matching in Docusaurus. When trying to process files, I'm getting an error that says the file path was not contained in any of the root folders, even though the file is clearly inside one of the specified root folders.

### Reproduction

```js
const matcher = createAbsoluteFilePathMatcher(
  ['**/*.md'],
  ['/path/to/docs']
);

// This throws an error unexpectedly
matcher('/path/to/docs/intro.md');
```

The error message I get is:
```
createAbsoluteFilePathMatcher unexpected error, absoluteFilePath=/path/to/docs/intro.md was not contained in any of the root folders: /path/to/docs
```

### Expected behavior

The matcher should successfully match files that are within the specified root folders without throwing errors. The file `/path/to/docs/intro.md` is clearly inside the `/path/to/docs` folder, so it should work correctly.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
