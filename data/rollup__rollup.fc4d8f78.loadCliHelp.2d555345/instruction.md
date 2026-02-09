# Bug Report

### Describe the bug

When loading CLI help files, the plugin is incorrectly matching files that contain 'help.md' anywhere in their path, not just files that end with 'help.md'. This causes unintended files to be processed by the loader.

### Reproduction

```js
// Any file path containing 'help.md' will be matched
// For example:
// - /some/path/help.md/other-file.js  ❌ (should not match)
// - /help.md-backup/file.js  ❌ (should not match)
// - /actual/help.md  ✓ (should match)
```

Create a file structure where 'help.md' appears in a directory name or middle of a filename:
1. Create a directory like `help.md.backup/`
2. Place any file inside it
3. The loader will incorrectly attempt to process it

### Expected behavior

The loader should only match files that actually end with 'help.md', not files where 'help.md' appears anywhere in the path.

### Additional context

This issue appears to have been introduced in a recent change to the file matching logic. The current implementation using `includes()` is too broad and will cause false positives.

---
Repository: /testbed
