# Bug Report

### Describe the bug

The `readingTime` function in the blog plugin is returning unexpected values. When I try to use the default reading time calculation, it seems like the function is now returning the content string itself instead of the calculated reading time.

### Reproduction

```js
// In docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-blog',
      {
        // Using default readingTime option
        readingTime: ({content, defaultReadingTime}) => defaultReadingTime({content}),
      },
    ],
  ],
};
```

When rendering blog posts, the reading time shows the entire content string instead of a number (like "5 min read").

### Expected behavior

The `defaultReadingTime` function should be called with the content and return a calculated reading time value (e.g., a number representing minutes), not the raw content string.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
