# Bug Report

### Describe the bug

I'm experiencing an issue with the client redirects plugin where extension-based redirects are not working as expected. When I have a file with an extension like `.html` or `.md`, the redirect behavior seems to be inverted or completely broken.

### Reproduction

Here's what I'm seeing:

1. Set up extension redirects in the plugin config:
```js
{
  fromExtensions: ['html', 'md']
}
```

2. Create a page at `/docs/my-page`

3. Try to access `/docs/my-page.html`

Expected: Should redirect from `/docs/my-page.html` to `/docs/my-page`
Actual: The redirect doesn't work at all, or behaves in the opposite direction

It seems like the plugin is checking for extensions at the wrong end of the path and potentially reversing the redirect direction. This is causing pages with extensions to not redirect properly to their extensionless counterparts.

### Expected behavior

When `fromExtensions` is configured, accessing a URL with that extension (e.g., `/page.html`) should redirect to the URL without the extension (`/page`).

### System Info

- Docusaurus version: Latest
- Plugin: @docusaurus/plugin-client-redirects

This is breaking our migration from an old static site where all URLs had `.html` extensions. Users bookmarked those URLs and now they're not being redirected properly.

---
Repository: /testbed
