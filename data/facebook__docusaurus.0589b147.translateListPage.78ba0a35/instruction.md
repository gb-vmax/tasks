# Bug Report

### Describe the bug

I'm experiencing an issue with blog list page translations. When I set up custom translations for my blog, the description is being replaced with the title translation instead of using the actual description translation.

### Reproduction

1. Configure a blog with custom translations in `i18n/[locale]/docusaurus-plugin-content-blog/options.json`:
```json
{
  "title": {
    "message": "My Custom Blog Title"
  },
  "description": {
    "message": "My Custom Blog Description"
  }
}
```

2. Build the site and check the blog list page metadata

3. Notice that both the title AND description are set to "My Custom Blog Title"

### Expected behavior

The blog list page should use the translated description message for `blogDescription`, not the title message. Both fields should have their respective translated values.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
