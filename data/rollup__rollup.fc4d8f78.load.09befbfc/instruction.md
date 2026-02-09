# Bug Report

### Describe the bug

I'm encountering an issue with the stdin plugin where it's not properly handling module IDs. When trying to load modules via stdin with certain ID patterns, the plugin fails to recognize and load them correctly.

### Reproduction

```js
// Try loading a module with stdin and a suffix
// For example, when using: rollup -p stdin.js

// The plugin should match IDs like:
// - "-"
// - "-.js"
// - "-.ts"

// But it seems to be doing the comparison backwards
```

When I use stdin with a file extension suffix (e.g., `stdin.js`), the module loading doesn't work as expected. The ID matching logic appears to be checking the wrong string against the pattern.

### Expected behavior

The stdin plugin should correctly identify and load modules when:
1. The ID is exactly the stdin name (`-`)
2. The ID starts with the stdin name followed by a dot (e.g., `-.js`, `-.ts`)

The module should load successfully in both cases.

### System Info
- Rollup version: latest
- Node version: 18+

---
Repository: /testbed
