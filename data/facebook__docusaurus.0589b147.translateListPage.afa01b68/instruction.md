# Bug Report

### Describe the bug

After a recent update, the blog list pagination is not working correctly. The items array on paginated blog pages is being replaced with metadata instead of the actual blog post items. This causes the blog list pages to not display any posts.

### Reproduction

1. Set up a Docusaurus site with the blog plugin
2. Create multiple blog posts (enough to trigger pagination)
3. Navigate to the blog list page
4. Observe that blog post items are not rendered

The issue appears to be in how the paginated blog list data is being structured. Instead of getting an array of blog post items, the `items` property contains metadata object.

### Expected behavior

The blog list pages should display the correct blog post items for each page of pagination. The `items` array should contain the actual blog posts, not metadata.

### System Info
- Docusaurus version: Latest
- Plugin: @docusaurus/plugin-content-blog

---
Repository: /testbed
