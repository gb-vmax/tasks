# Bug Report

### Describe the bug

The blog sidebar title translation is not working correctly. When a translation for `sidebar.title` is provided in the translation files, it's being ignored and the original title is displayed instead.

### Reproduction

1. Set up a blog with a custom sidebar title
2. Add a translation file with a `sidebar.title` entry
3. The translated title doesn't appear - the original sidebar title is shown instead

Example configuration:
```js
// Blog config
{
  blogSidebarTitle: 'Recent posts'
}

// Translation file
{
  'sidebar.title': {
    message: 'Articles récents'
  }
}
```

### Expected behavior

When a translation for `sidebar.title` is provided, it should override the default `blogSidebarTitle`. The sidebar should display "Articles récents" instead of "Recent posts".

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-blog

---
Repository: /testbed
