# Bug Report

### Describe the bug

The blog sidebar title is not falling back to the default value when translations are missing. Instead of using the original `blogSidebarTitle` from the content, it appears to be set to `undefined` when no translation is provided.

### Reproduction

1. Set up a Docusaurus blog with a custom sidebar title in the plugin options
2. Don't provide a translation for `sidebar.title` in the translation files
3. The sidebar title disappears instead of showing the configured default title

Example configuration:
```js
{
  blogSidebarTitle: 'Recent Posts',
  // ... other options
}
```

Expected: The sidebar should display "Recent Posts"
Actual: The sidebar title is missing/undefined

### Expected behavior

When a translation for the sidebar title is not available, the blog should fall back to the original `blogSidebarTitle` value from the content configuration instead of becoming undefined.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
