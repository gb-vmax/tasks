# Bug Report

### Describe the bug

I'm experiencing an issue with extension-based redirects in the client redirects plugin. It seems like the redirect logic is inverted - paths that should have redirects don't get them, and paths that shouldn't have redirects are getting them instead.

### Reproduction

When I have a path like `/docs/intro.html`, the plugin should create a redirect from `/docs/intro` to `/docs/intro.html`. However, this redirect is not being created.

Conversely, when I have a path without an extension like `/docs/intro`, the plugin is unexpectedly trying to create a redirect from `/docs/intro` to something like `/docs/intr` (with the first extension removed from the path).

Steps to reproduce:
1. Configure the plugin with extensions like `.html`
2. Create a page with a dotted extension (e.g., `intro.html`)
3. The expected redirect from the extensionless path is not created
4. Pages without extensions get incorrect redirects applied

### Expected behavior

- Paths with recognized extensions (like `.html`) should generate redirects FROM the extensionless version TO the versioned path
- Paths without extensions should not generate any redirects
- Example: `/docs/intro.html` should create a redirect from `/docs/intro` → `/docs/intro.html`

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

---
Repository: /testbed
