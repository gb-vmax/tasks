# Bug Report

### Describe the bug

The translation keys for generated-index sidebar categories are swapped. When a category has a `link` of type `generated-index` with both `title` and `description` fields, the translation file generates keys with the wrong content - the title gets assigned to the description key and vice versa.

### Reproduction

Create a sidebar configuration with a generated-index category:

```js
{
  type: 'category',
  label: 'My Category',
  link: {
    type: 'generated-index',
    title: 'Category Overview',
    description: 'This is the category description'
  },
  items: [...]
}
```

When generating translation files, the output will have:
- `sidebar.mySidebar.category.My Category.link.generated-index.title` containing "This is the category description"
- `sidebar.mySidebar.category.My Category.link.generated-index.description` containing "Category Overview"

### Expected behavior

The translation keys should match their content:
- `sidebar.mySidebar.category.My Category.link.generated-index.title` should contain the title value
- `sidebar.mySidebar.category.My Category.link.generated-index.description` should contain the description value

This makes it confusing when translating content since the key names don't match what they're actually translating.

---
Repository: /testbed
