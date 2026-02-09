# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar translations where the translated content is not being generated correctly. It seems like the sidebar items themselves are not being passed to the translation function, only the sidebar names are being used.

### Reproduction

1. Set up a Docusaurus site with multiple sidebars defined in `sidebars.js`
2. Configure the docs plugin with versioning enabled
3. Try to extract translations for the sidebars
4. Notice that the translation files don't contain the actual sidebar item translations

Example configuration:
```js
// sidebars.js
module.exports = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      items: ['intro', 'installation'],
    },
  ],
  apiSidebar: [
    {
      type: 'category', 
      label: 'API Reference',
      items: ['api/overview'],
    },
  ],
};
```

When running the translation extraction, the sidebar category labels and item titles are not being included in the translation files.

### Expected behavior

The translation files should include all translatable strings from the sidebar definitions, including category labels, link labels, and other sidebar item content. Each sidebar's actual structure and content should be processed for translation extraction.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
