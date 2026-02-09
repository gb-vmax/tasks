# Bug Report

### Describe the bug

When using blog list pagination with custom translations, the `blogTitle` and `blogDescription` from translations are being overwritten by the original metadata values. The translated title and description appear briefly but then get replaced by the default values.

### Reproduction

```js
// In your blog plugin configuration with translations
const translations = {
  title: { message: 'My Translated Blog Title' },
  description: { message: 'My Translated Blog Description' }
};

// When the blog list page is rendered, the metadata shows:
// Expected: blogTitle = 'My Translated Blog Title'
// Actual: blogTitle = original untranslated value
```

Steps to reproduce:
1. Configure a blog with custom translations for title and description
2. Set translated messages for `title` and `description`
3. Navigate to the blog list page
4. The page shows the original title/description instead of the translated ones

### Expected behavior

The translated `blogTitle` and `blogDescription` should take precedence and be displayed on the blog list pages. The translation values should not be overwritten by the original metadata.

### System Info
- Docusaurus plugin: @docusaurus/plugin-content-blog
- Observed on latest version

---
Repository: /testbed
