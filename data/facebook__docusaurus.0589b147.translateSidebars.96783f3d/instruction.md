# Bug Report

### Describe the bug

I'm encountering an issue with sidebar translations where the sidebar structure appears to be corrupted. When trying to use translated sidebars, the sidebar items are not rendering correctly and the sidebar name seems to be getting replaced with the wrong data.

### Reproduction

```js
const version = {
  sidebars: {
    tutorialSidebar: [
      { type: 'doc', id: 'intro' },
      { type: 'doc', id: 'getting-started' }
    ],
    apiSidebar: [
      { type: 'category', label: 'API', items: [...] }
    ]
  }
};

// When translateSidebars is called, the sidebar structure breaks
const translatedSidebars = translateSidebars(version, sidebarsTranslations);
// Expected: sidebars with correct structure
// Actual: sidebar items and names are mixed up
```

### Expected behavior

The `translateSidebar` function should receive:
- `sidebar`: the actual sidebar array with items
- `sidebarName`: the string name of the sidebar (e.g., 'tutorialSidebar', 'apiSidebar')

Instead, it seems like the parameters are being passed incorrectly, causing the sidebar structure to break during translation.

### System Info

- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
