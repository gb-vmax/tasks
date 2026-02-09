# Bug Report

### Describe the bug

Files are not being written when their content changes. It seems like the file generation logic is inverted - files are only written when the content hash matches the previous hash, but they should be written when the content has actually changed.

### Reproduction

```js
// First generation
await generate(
  generatedFilesDir,
  'example.js',
  'const foo = "initial";',
  false
);

// Try to update with new content
await generate(
  generatedFilesDir,
  'example.js',
  'const foo = "updated";',
  false
);

// The file still contains "initial" instead of "updated"
```

### Expected behavior

When the content changes, the file should be overwritten with the new content. The file should only be skipped if the hash matches (meaning the content hasn't changed).

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
