# Bug Report

### Describe the bug

When using the blog plugin, the blog list page metadata is not being set correctly. The `blogDescription` field is incorrectly falling back to `blogTitle` instead of the actual blog description, and the metadata spread is using the wrong object reference.

### Reproduction

```js
// In a Docusaurus blog configuration
const blogListPage = {
  metadata: {
    blogTitle: 'My Tech Blog',
    blogDescription: 'A blog about web development and JavaScript'
  }
}

// When translations are not provided, the description fallback uses the title
// Result: blogDescription = 'My Tech Blog' (wrong!)
// Expected: blogDescription = 'A blog about web development and JavaScript'
```

### Steps to reproduce
1. Set up a Docusaurus blog with a custom blog title and description
2. Don't provide translation overrides for description
3. Check the metadata on the blog list page
4. Notice that `blogDescription` has the same value as `blogTitle`

### Expected behavior

The `blogDescription` should fall back to `page.metadata.blogDescription`, not `page.metadata.blogTitle`. Also, the metadata spread should use `metadata` instead of `page`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
