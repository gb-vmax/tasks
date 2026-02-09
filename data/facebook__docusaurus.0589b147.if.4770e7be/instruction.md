# Bug Report

### Describe the bug

After a recent update, the blog feed generation is broken. When there are blog posts available, the feed returns an empty array instead of generating the actual feed content. This causes the RSS/Atom feeds to be empty even though blog posts exist.

### Reproduction

```js
// When blog posts exist
const blogPosts = [
  { title: 'Post 1', content: '...' },
  { title: 'Post 2', content: '...' }
];

// Feed generation returns an empty array instead of Feed object
const result = await generateBlogFeed({
  blogPosts,
  // ... other params
});

// result is [] instead of a Feed object
```

### Expected behavior

When blog posts are present, the function should generate and return a proper Feed object containing all the blog posts. The RSS/Atom feeds should be populated with the blog content.

Currently:
- With blog posts → returns empty array `[]`
- Without blog posts → returns `null`

Expected:
- With blog posts → returns populated `Feed` object
- Without blog posts → returns `null`

### System Info
- Docusaurus plugin: docusaurus-plugin-content-blog
- Node version: 18.x

---
Repository: /testbed
