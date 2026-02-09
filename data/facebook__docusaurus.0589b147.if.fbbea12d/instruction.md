# Bug Report

### Describe the bug

Sidebars are not loading properly and showing as disabled even when the sidebar file exists. After a recent update, my documentation sidebar disappeared completely and the docs are rendering without any navigation.

### Reproduction

1. Create a Docusaurus project with a valid `sidebars.js` or `sidebars.ts` file
2. Add some sidebar configuration (e.g., categories, links, etc.)
3. Run the dev server
4. Notice that the sidebar doesn't appear at all

Here's my setup:

```js
// sidebars.js
module.exports = {
  docs: [
    'intro',
    {
      type: 'category',
      label: 'Guides',
      items: ['guide1', 'guide2'],
    },
  ],
};
```

The file exists in the correct location, but it's being treated as if it doesn't exist.

### Expected behavior

The sidebar should load and display normally when a valid sidebar configuration file is present. The navigation should appear on the left side of the documentation pages.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This is blocking our documentation site from being usable. Any help would be appreciated!

---
Repository: /testbed
