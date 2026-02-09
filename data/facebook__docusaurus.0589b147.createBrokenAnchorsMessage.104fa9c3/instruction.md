# Bug Report

### Describe the bug

I'm experiencing an issue with broken anchor link detection in my Docusaurus site. When I have broken anchors on a single page, no warning or error message is being displayed during the build process. The broken anchor detection seems to only work when there are broken anchors on multiple pages.

### Reproduction

1. Create a Docusaurus site with a single page containing broken anchor links
2. Add links like `[link](#non-existent-anchor)` that point to anchors that don't exist
3. Run the build
4. Notice that no broken anchor warnings are shown

However, if I add broken anchors to a second page, then the warnings appear for both pages.

### Expected behavior

The build should report broken anchor links even when they only exist on a single page. Currently it seems like the threshold is set too high - it should warn about broken anchors regardless of how many pages are affected.

### Additional context

This is problematic because broken anchors on a single page can go unnoticed during development and end up in production. The broken link checker should catch these issues consistently.

---
Repository: /testbed
