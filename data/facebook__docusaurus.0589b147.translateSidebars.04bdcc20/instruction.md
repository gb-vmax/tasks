# Bug Report

### Describe the bug

When using translated sidebars in a versioned docs plugin, the sidebar structure becomes corrupted. Instead of translating the actual sidebar items, the system appears to be using the translation file content as the source, which causes sidebar items to disappear or be replaced with incorrect content.

### Reproduction

```js
// Setup a versioned docs plugin with translations
const version = {
  sidebars: {
    tutorialSidebar: [
      { type: 'doc', id: 'intro' },
      { type: 'doc', id: 'tutorial' }
    ],
    apiSidebar: [
      { type: 'doc', id: 'api-reference' }
    ]
  }
}

const sidebarsTranslations = {
  tutorialSidebar: {
    'sidebar.tutorialSidebar.category.Getting Started': {
      message: 'Démarrage'
    }
  }
  // Note: apiSidebar is not in translations
}

// After translation, apiSidebar disappears completely
// Only sidebars present in the translation file are kept
```

### Expected behavior

All sidebars from the version should be preserved and translated. Sidebars that don't have translations should remain unchanged. The translation process should iterate over the actual version sidebars, not the translation file keys.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
