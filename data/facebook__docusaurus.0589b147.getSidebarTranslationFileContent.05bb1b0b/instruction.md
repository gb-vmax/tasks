# Bug Report

### Describe the bug

When generating translation files for sidebars with categories that have generated-index links, the title and description fields are being swapped. The translation key for `title` contains the `description` value and vice versa.

### Reproduction

Create a sidebar configuration with a category that has a generated-index link:

```js
{
  type: 'category',
  label: 'My Category',
  link: {
    type: 'generated-index',
    title: 'Category Overview',
    description: 'This is the description for the category'
  },
  items: [...]
}
```

When the translation file is generated, the values are incorrectly mapped:
- `sidebar.mySidebar.category.My Category.link.generated-index.title` gets the description value
- `sidebar.mySidebar.category.My Category.link.generated-index.description` gets the title value

### Expected behavior

The translation keys should correctly map to their corresponding values:
- Title key should contain the title value
- Description key should contain the description value

This makes it confusing when translating content as the values don't match their keys.

---
Repository: /testbed
