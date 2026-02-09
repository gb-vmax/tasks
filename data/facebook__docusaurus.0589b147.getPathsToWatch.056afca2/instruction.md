# Bug Report

### Describe the bug

When using the docs plugin with multiple include patterns, the file watching behavior seems broken. Files that should trigger rebuilds are not being watched properly.

### Reproduction

Set up a Docusaurus project with the following docs plugin configuration:

```js
{
  id: 'default',
  include: ['**/*.md', '**/*.mdx'],
  // ... other options
}
```

Expected: All markdown and MDX files should be watched for changes
Actual: Only some files are being watched, hot reload doesn't work consistently

### Expected behavior

All files matching the include patterns should be watched and trigger rebuilds when modified. The sidebar file should also be watched if it exists.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
