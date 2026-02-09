# Bug Report

### Describe the bug

After a recent update, the sidebar translations are not being generated correctly. When I run the translation extraction, some sidebar items that should be translatable are missing from the generated translation files, while items that shouldn't be translatable are being included instead.

### Reproduction

1. Create a sidebar with multiple categories and doc items
2. Mark some doc items as translatable and others as non-translatable
3. Run the translation extraction process
4. Check the generated translation file

Expected: Only translatable items should appear in the translation file
Actual: Non-translatable items are included, and translatable ones are missing

Here's a sample sidebar config:
```js
{
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        {
          type: 'doc',
          id: 'intro',
          label: 'Introduction',
          translatable: true
        },
        {
          type: 'doc',
          id: 'api-reference',
          label: 'API',
          translatable: false
        }
      ]
    }
  ]
}
```

In this case, "Introduction" should be in the translation file but isn't, while "API" shouldn't be there but is.

### Expected behavior

The translation file should only contain entries for sidebar items where `translatable` is `true` (or not explicitly set to `false`). Non-translatable items should be excluded.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
