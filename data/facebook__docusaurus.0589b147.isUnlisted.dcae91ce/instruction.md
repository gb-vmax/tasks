# Bug Report

### Describe the bug

I'm experiencing an issue with blog tag visibility when using the `docusaurus-plugin-content-blog` plugin. Tags that should be visible are not showing up correctly, and the plugin seems to be checking the wrong property path for unlisted status.

### Reproduction

```js
// Blog post with unlisted metadata
const blogPost = {
  metadata: {
    unlisted: true,
    // ... other metadata
  }
}

// When getBlogTags processes this post, the tag visibility 
// is calculated incorrectly and tags don't appear as expected
```

Steps to reproduce:
1. Create a blog post with `unlisted: true` in the frontmatter
2. Assign tags to the post
3. Build the site
4. The tag visibility is not determined correctly

### Expected behavior

Tags should be properly visible/hidden based on whether blog posts are unlisted. The plugin should correctly check `item.metadata.unlisted` to determine if a post is unlisted.

### System Info

- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-blog

---
Repository: /testbed
