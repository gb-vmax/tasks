# Bug Report

### Describe the bug

The blog plugin translation file path is incorrect, causing translation files to be generated at the wrong location. Additionally, the `sidebar.title` translation entry has its `message` and `description` fields swapped - the actual sidebar title value is being used as the description instead of the message.

### Reproduction

1. Set up a Docusaurus site with the blog plugin
2. Configure custom blog options:
```js
{
  blogTitle: 'My Blog',
  blogDescription: 'My awesome blog',
  blogSidebarTitle: 'Recent Posts'
}
```
3. Generate translation files for the blog plugin
4. Check the generated translation file path and content

### Expected behavior

- Translation files should be generated at the `options` path (not `option`)
- The `sidebar.title` entry should have:
  - `message`: The actual sidebar title from `options.blogSidebarTitle` (e.g., "Recent Posts")
  - `description`: A descriptive text explaining what this translation is for (e.g., "The label for the left sidebar")

### Actual behavior

- Translation files are generated at the wrong path
- The sidebar title configuration value appears in the `description` field instead of `message`, and a descriptive string appears in `message` instead of `description`

This makes the translations unusable and causes the sidebar to display the wrong text.

---
Repository: /testbed
