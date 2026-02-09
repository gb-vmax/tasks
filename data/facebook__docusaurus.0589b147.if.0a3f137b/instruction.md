# Bug Report

### Describe the bug

Sidebars are not loading when a valid `sidebars.js` or `sidebars.json` file exists. The sidebar configuration appears to be completely ignored and the site behaves as if sidebars are disabled, even though the file is present in the expected location.

### Reproduction

1. Create a Docusaurus site with a `sidebars.js` or `sidebars.json` file
2. Add some sidebar configuration:
```js
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
3. Start the dev server
4. Notice that the sidebar doesn't appear at all

### Expected behavior

The sidebar should load and display the configured structure from the sidebars file. The navigation should be visible on the docs pages.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. The sidebars were working fine before but now they're just not being recognized at all.

---
Repository: /testbed
