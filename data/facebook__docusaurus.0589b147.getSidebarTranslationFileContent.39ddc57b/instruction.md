# Bug Report

### Describe the bug

The sidebar translation keys are being generated incorrectly for category links with generated-index type. The translation keys are missing the category label in the path, which causes translation files to have incorrect or conflicting keys when multiple categories have generated-index links.

### Reproduction

1. Create a sidebar with multiple categories that have `generated-index` links:

```js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      link: {
        type: 'generated-index',
        title: 'Welcome to Getting Started',
        description: 'Learn the basics'
      },
      items: [...]
    },
    {
      type: 'category',
      label: 'Advanced Topics',
      link: {
        type: 'generated-index',
        title: 'Advanced Guide',
        description: 'Deep dive into features'
      },
      items: [...]
    }
  ]
}
```

2. Run the translation extraction
3. Check the generated translation keys

### Expected behavior

Each category's generated-index link should have unique translation keys that include the category label:
- `sidebar.docs.category.Getting Started.link.generated-index.title`
- `sidebar.docs.category.Getting Started.link.generated-index.description`
- `sidebar.docs.category.Advanced Topics.link.generated-index.title`
- `sidebar.docs.category.Advanced Topics.link.generated-index.description`

### Actual behavior

All categories share the same translation keys without the category label:
- `sidebar.docs.link.generated-index.title`
- `sidebar.docs.link.generated-index.description`

This causes conflicts when you have multiple categories with generated-index links, and translations can't be properly managed for each category separately.

---
Repository: /testbed
