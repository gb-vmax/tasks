# Bug Report

### Describe the bug

When using versioned docs with multiple content paths, the file watcher is not correctly monitoring category metadata files (`_category_.json`/`_category_.yml`) in all content directories. Changes to category metadata files in secondary content paths are not being detected, requiring a full restart to see updates.

### Reproduction

1. Configure a docs plugin with multiple content paths:
```js
{
  id: 'docs',
  path: 'docs',
  include: ['**/*.md'],
  // ... other options
}
```

2. Set up versioned docs with additional content paths (e.g., via `contentPathLocalized` or similar)
3. Create a `_category_.json` file in a secondary content path
4. Start the dev server
5. Modify the `_category_.json` file in the secondary content path
6. Notice that the changes are not reflected without restarting the server

### Expected behavior

All category metadata files across all content paths should be watched and trigger hot reload when modified, similar to how markdown files are watched.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The sidebar file path watching also seems to have changed behavior - it's now being added with `push` instead of `unshift`, though I'm not sure if that's related to the main issue.

---
Repository: /testbed
