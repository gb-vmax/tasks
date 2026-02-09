# Bug Report

### Describe the bug

I'm experiencing an issue where files are not being written/updated when they should be. It seems like the file generation logic is inverted - files are only written when the content hash matches the existing file, but they should be written when the content has actually changed.

### Reproduction

```js
// First write
await generate(filepath, 'content A', false);
// File is written correctly

// Update with different content
await generate(filepath, 'content B', false);
// File should be updated but isn't

// The file still contains 'content A' instead of 'content B'
```

### Expected behavior

When calling `generate()` with new content that differs from the existing file content, the file should be overwritten with the new content. Currently, it appears that files are only being written when the content hash is the same as what's already on disk, which is the opposite of what should happen.

### Additional context

This is causing issues in my build process where updated content isn't being reflected in the output files. The cache mechanism seems to be preventing necessary file updates.

---
Repository: /testbed
