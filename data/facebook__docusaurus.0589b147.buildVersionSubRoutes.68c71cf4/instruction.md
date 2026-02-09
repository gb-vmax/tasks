# Bug Report

### Describe the bug

I'm experiencing an issue where the docs plugin seems to be loading routes in an unexpected order, and sometimes routes are missing or not being generated correctly. The sidebar and tag routes appear to be racing against each other instead of loading properly.

### Reproduction

This happens when building a Docusaurus site with the docs plugin configured with multiple versions and tags.

Steps to reproduce:
1. Set up a Docusaurus project with versioned docs
2. Add tags to your documentation pages
3. Build the site
4. Notice that sometimes the sidebar routes or tag routes are incomplete or missing

The behavior is inconsistent - sometimes it works, sometimes it doesn't. It seems like there's some kind of race condition happening during the route building process.

### Expected behavior

Both sidebar routes and tag routes should be generated reliably and consistently every time the site is built. The routes should be loaded in a predictable manner without any race conditions.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
