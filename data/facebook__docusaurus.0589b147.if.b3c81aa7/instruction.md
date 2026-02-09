# Bug Report

### Describe the bug

I'm experiencing an issue with blog feed generation where the function returns an empty array instead of `null` when there are no blog posts. This breaks the expected return type and causes problems downstream when the code expects either a `Feed` object or `null`.

### Reproduction

```js
// When there are no blog posts
const feed = await generateBlogFeed({
  blogPosts: [],
  // ... other options
});

// Expected: feed === null
// Actual: feed === []
```

The function signature indicates it should return `Promise<Feed | null>`, but it's now returning an empty array when there are no posts.

### Expected behavior

When there are no blog posts, the function should return `null` (not an empty array) to maintain type consistency with the function signature.

### Additional context

This seems to have started happening recently. The return type mismatch could cause issues for any code that checks for `null` specifically or relies on the documented return type.

---
Repository: /testbed
