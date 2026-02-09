# Bug Report

### Describe the bug

After a recent update, the blog RSS/Atom feed is no longer being generated. The feed files that were previously created in the build output are now missing, even though blog posts exist and are being rendered correctly on the site.

### Reproduction

1. Set up a Docusaurus site with the blog plugin enabled
2. Add one or more blog posts to the `blog/` directory
3. Configure feed options in `docusaurus.config.js`:
```js
{
  blog: {
    feedOptions: {
      type: 'all',
      title: 'My Blog',
    }
  }
}
```
4. Build the site
5. Check the output directory for feed files (e.g., `rss.xml`, `atom.xml`)

### Expected behavior

Feed files should be generated when blog posts are present. The RSS/Atom feeds should contain entries for all published blog posts.

### Actual behavior

No feed files are generated even when blog posts exist. The build completes successfully but the feeds are missing from the output.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
