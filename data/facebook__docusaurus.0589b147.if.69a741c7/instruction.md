# Bug Report

### Describe the bug

The blog feed generation is failing when there's exactly one blog post. Instead of generating a valid feed, it returns an empty array, which causes issues downstream.

### Reproduction

1. Create a Docusaurus site with the blog plugin enabled
2. Add exactly one blog post to your blog
3. Build the site
4. Check the generated RSS/Atom feed

The feed generation returns an empty array instead of a valid Feed object, breaking the feed functionality.

### Expected behavior

When there's one blog post, the feed should still be generated correctly. A feed with a single post is valid and should be created. Only when there are zero posts should the feed generation be skipped.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
