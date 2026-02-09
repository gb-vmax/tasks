# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar translations where the sidebar names and content appear to be swapped or incorrectly mapped. After recent changes, the translation keys being generated don't match the actual sidebar structure, causing translations to fail or be applied to the wrong sidebars.

### Reproduction

When setting up a docs plugin with multiple sidebars like this:

```js
sidebars: {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      items: ['intro', 'setup'],
    },
  ],
  apiSidebar: [
    {
      type: 'category', 
      label: 'API Reference',
      items: ['api/overview'],
    },
  ],
}
```

The translation file generation seems to mix up the sidebar names with the sidebar content, resulting in incorrect translation keys or the translations being applied to the wrong sidebar.

### Expected behavior

The translation keys should correctly correspond to their respective sidebars (tutorialSidebar, apiSidebar, etc.) and the sidebar content should be properly associated with the correct sidebar name.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
