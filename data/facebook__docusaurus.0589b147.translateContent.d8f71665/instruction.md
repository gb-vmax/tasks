# Bug Report

### Describe the bug

The blog sidebar title translation is not falling back to the original content title when a translation is missing. Instead, it seems to be checking the translation twice and never using the actual `content.blogSidebarTitle` value as a fallback.

### Reproduction

1. Set up a Docusaurus blog with a custom sidebar title in the config
2. Create a translation file that doesn't include the `sidebar.title` key
3. Build the site with the translation locale

Expected: The sidebar should show the original title from the blog config
Actual: The sidebar title appears to be undefined or missing

### Example

```js
// blog config
{
  blogSidebarTitle: 'My Recent Posts'
}

// translation file (missing sidebar.title key)
{
  'post.readMore': 'Lire la suite'
}
```

The sidebar title doesn't appear at all instead of showing "My Recent Posts".

### Additional context

This seems to affect the fallback behavior when translations are incomplete. The original content value should be used when a translation key is not found.

---
Repository: /testbed
