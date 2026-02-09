# Bug Report

### Describe the bug

The versioned sidebars file path is incorrect when using the docs plugin. The generated filename doesn't match the expected pattern, causing sidebars to not load properly for versioned documentation.

### Reproduction

```js
// With a docs plugin configuration
{
  id: 'api',
  path: 'docs/api',
  // ... other options
}

// When creating a new version
// Expected file: versioned_sidebars/version-1.0.0-sidebars.json
// Actual file being looked up: versioned_sidebars/1.0.0-api-sidebars.json
```

Steps to reproduce:
1. Set up a Docusaurus site with a docs plugin that has a custom plugin ID
2. Create a versioned documentation (e.g., version 1.0.0)
3. Notice that the sidebars file is not being found/loaded correctly

### Expected behavior

The versioned sidebars file should be located at `versioned_sidebars/version-{versionName}-sidebars.json` regardless of the plugin ID. The current behavior seems to be generating a different filename pattern that breaks the loading mechanism.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
