# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where the version routes are not being built correctly. When navigating through versioned documentation, some routes appear to be missing or incomplete - specifically, either the sidebar route or the tags routes are present, but not both.

### Reproduction

1. Set up a Docusaurus site with versioned docs
2. Configure the docs plugin with multiple versions
3. Add tags to some documentation pages
4. Build the site and navigate to a versioned docs page
5. Notice that either the sidebar navigation or the tags pages are missing/broken

The issue seems to affect the route generation for versioned documentation. Sometimes I see the sidebar working but tags pages return 404, other times it's the opposite.

### Expected behavior

Both the sidebar routes and tags routes should be available for each documentation version. All versioned documentation pages should be accessible with proper navigation and tag filtering capabilities.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
