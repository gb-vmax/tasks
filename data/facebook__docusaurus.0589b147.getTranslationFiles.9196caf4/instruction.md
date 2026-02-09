# Bug Report

### Describe the bug

The blog sidebar title is showing the wrong value. When I configure my blog plugin with a custom `blogSidebarTitle`, it's being replaced with the `blogTitle` instead. This means the sidebar always shows the same title as the main blog title, even when I want them to be different.

### Reproduction

In `docusaurus.config.js`:

```js
{
  plugins: [
    [
      '@docusaurus/plugin-content-blog',
      {
        blogTitle: 'My Awesome Blog',
        blogSidebarTitle: 'Recent Posts',
        // ... other options
      },
    ],
  ],
}
```

**Expected:** The sidebar should display "Recent Posts"  
**Actual:** The sidebar displays "My Awesome Blog"

### Additional context

This seems to affect the translation files generation. The sidebar title option is not being respected and defaults to using the main blog title instead.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
