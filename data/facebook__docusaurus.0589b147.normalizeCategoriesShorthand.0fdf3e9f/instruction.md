# Bug Report

### Describe the bug

I'm experiencing an issue with sidebar category configuration when using the shorthand syntax. The category labels and items seem to be swapped, and the generated sidebar structure is incorrect.

### Reproduction

```js
const sidebar = {
  'Getting Started': ['intro', 'installation'],
  'Advanced': ['configuration', 'api']
}
```

When using this shorthand format, the sidebar renders with the wrong labels. Instead of showing "Getting Started" and "Advanced" as category labels, it's showing the item arrays as labels and the intended labels as items.

### Expected behavior

The shorthand syntax should correctly map the object keys to category labels and the values to the items array. Categories should be created with proper labels that match the keys in the configuration object.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
