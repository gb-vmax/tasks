# Bug Report

### Describe the bug

Sidebars are not loading properly - they appear to be completely disabled even when a valid `sidebars.js` file exists in the project. The documentation navigation just doesn't show up at all.

### Reproduction

1. Create a Docusaurus project with a standard `sidebars.js` file
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
4. Navigate to any docs page

### Expected behavior

The sidebar should render with the configured navigation structure. Instead, no sidebar appears at all, as if the sidebars file doesn't exist.

This is blocking our entire documentation site from working. Any help would be appreciated!

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
