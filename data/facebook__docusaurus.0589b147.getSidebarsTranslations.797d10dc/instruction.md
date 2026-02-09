# Bug Report

### Describe the bug

When generating translation files for sidebars, the sidebar content is not being passed correctly to `getSidebarTranslationFileContent`. Instead of passing the actual sidebar object, the sidebar name is being passed twice as both arguments.

### Reproduction

```js
// Given a version with sidebars like:
const version = {
  sidebars: {
    tutorialSidebar: {
      items: [
        { type: 'doc', id: 'intro' },
        { type: 'category', label: 'Tutorial', items: [...] }
      ]
    },
    apiSidebar: {
      items: [...]
    }
  }
}

// When getSidebarsTranslations is called
// It incorrectly passes sidebarName twice instead of (sidebar, sidebarName)
```

### Expected behavior

The function should pass both the sidebar object and its name to `getSidebarTranslationFileContent` so that the actual sidebar structure can be processed for translations. Currently it's passing the sidebar name as both parameters, which means the translation extraction won't have access to the actual sidebar items and their labels.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
