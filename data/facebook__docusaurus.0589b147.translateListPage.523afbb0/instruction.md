# Bug Report

### Describe the bug

When using translations for blog list pages, the `blogTitle` and `blogDescription` metadata fields are not respecting the translation values properly. Instead of using the translated title/description when available, the metadata values are being used as the primary source, with translations only as fallback.

### Reproduction

1. Set up a Docusaurus site with the blog plugin
2. Configure translations for a blog list page with custom `title` and `description` messages
3. The blog list page displays the original metadata values instead of the translated ones

Expected behavior: When translations are provided via the `title` and `description` messages, they should take precedence over the default metadata values.

Actual behavior: The metadata values are used first, and translations are only used as fallback when metadata is not available.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-blog

This appears to be a regression where the priority order for title and description was reversed - translations should override the default metadata, not the other way around.

---
Repository: /testbed
