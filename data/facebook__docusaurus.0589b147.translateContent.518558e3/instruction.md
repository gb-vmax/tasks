# Bug Report

### Describe the bug

I'm experiencing an issue with blog sidebar title translations in the Docusaurus blog plugin. When I set up translations for my blog, the sidebar title is not being translated correctly. Instead of showing the translated sidebar title, it seems to be falling back to some unexpected value.

### Reproduction

1. Set up a Docusaurus site with the blog plugin
2. Configure translations for the blog sidebar title in your translation files
3. Add a custom `sidebar.title` translation message
4. Build/serve the site

The sidebar title doesn't display the translated text as expected. It appears to be using a different fallback value instead of the original `blogSidebarTitle`.

### Expected behavior

When a translation for `sidebar.title` is provided, it should be used. If no translation is available, it should fall back to the original `content.blogSidebarTitle` value, not something else.

### System Info
- Docusaurus version: latest
- Node version: 18.x

Has anyone else encountered this? The translations were working fine in previous versions.

---
Repository: /testbed
