# Bug Report

### Describe the bug

The `getFileLastUpdate` function is returning `null` for all valid file paths instead of retrieving the actual last update information. It seems like the logic is inverted - when a file path is provided, it immediately returns `null` instead of proceeding to fetch the git information.

### Reproduction

```js
// Call getFileLastUpdate with a valid file path
const result = await getFileLastUpdate('/path/to/valid/file.md');

// Expected: { timestamp: 1234567890, author: 'John Doe' }
// Actual: null
```

This affects all documentation pages that should display last update timestamps and author information. The metadata simply doesn't show up even though the files are properly tracked in git.

### Expected behavior

When a valid file path is provided, the function should:
1. Execute the git commands to fetch last commit information
2. Return an object with `timestamp` and `author` properties
3. Only return `null` when the file path is empty/undefined or when git operations fail

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
