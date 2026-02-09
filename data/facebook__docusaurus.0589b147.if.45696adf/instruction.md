# Bug Report

### Describe the bug

I'm experiencing an issue with the client redirects plugin where extension-based redirects (like `.html`) are being generated for paths that shouldn't have them. It seems like the logic for determining when to create extension redirects is inverted.

### Reproduction

When configuring the plugin with `fromExtensions: ['html']`, redirects are being created for:
- Empty paths (`''`)
- Root path (`'/'`) 
- Paths that already end with extensions (e.g., `/page.html`)

But redirects are NOT being created for regular paths like `/about` or `/docs/intro`, which are the ones that actually need the `.html` extension redirects.

Expected behavior:
- `/about` should redirect to `/about.html`
- `/docs/intro` should redirect to `/docs/intro.html`

Actual behavior:
- No redirects are created for paths without extensions
- Redirects are incorrectly attempted for paths that already have extensions or are empty/root

### Steps to reproduce

1. Configure the client redirects plugin with extension redirects enabled
2. Create pages with standard paths (no extensions)
3. Build the site
4. Notice that extension-based redirects are missing for normal paths

This seems to have broken the intended functionality where paths without extensions should automatically get redirects to their extension versions.

---
Repository: /testbed
