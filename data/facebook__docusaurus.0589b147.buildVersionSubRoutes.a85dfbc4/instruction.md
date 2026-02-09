# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where the route structure seems to be broken. The sidebar route and tags routes appear to be in the wrong order or incorrectly structured.

### Reproduction

When building a docs site with both sidebar and tags enabled:

1. Create a versioned docs setup
2. Add some tags to your documentation pages
3. Build the site
4. Check the generated routes structure

The routes array doesn't match the expected structure - it looks like the sidebar route and tags routes are being returned in an unexpected format.

### Expected behavior

The version sub-routes should return an array with the sidebar route first, followed by the spread tags routes:
```js
[sidebarRoute, ...tagsRoutes]
```

Instead, it seems like the destructuring assignment and return statement don't match up properly, causing the routes to be structured incorrectly.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
