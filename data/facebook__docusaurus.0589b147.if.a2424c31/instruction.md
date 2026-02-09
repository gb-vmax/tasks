# Bug Report

### Describe the bug

I'm encountering an issue with the blog feed generation where the function returns an incorrect type when there are no blog posts. The feed generation appears to return an empty array instead of `null`, which causes type inconsistencies downstream.

### Reproduction

When a blog has no posts:

```js
// Blog with no posts
const blogPosts = [];

// Feed generation is called
const feed = await generateBlogFeed({
  blogPosts,
  options,
  siteConfig,
  outDir,
  locale
});

// Expected: feed should be null
// Actual: feed is an empty array []
```

### Expected behavior

When there are no blog posts, the `generateBlogFeed` function should return `null` to indicate that no feed should be generated. This maintains type consistency with the function's return type signature `Promise<Feed | null>`.

### System Info

- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-blog

---
Repository: /testbed
