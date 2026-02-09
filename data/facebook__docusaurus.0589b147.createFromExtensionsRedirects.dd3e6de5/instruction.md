# Bug Report

### Describe the bug

I'm experiencing an issue with the client redirects plugin where extension-based redirects are not being created properly. It seems like paths that should get redirect rules are being skipped entirely.

### Reproduction

When configuring the plugin with extensions like `.html`:

```js
{
  fromExtensions: ['html']
}
```

Expected behavior: A path like `/docs/intro` should create a redirect from `/docs/intro.html` to `/docs/intro`

What actually happens: No redirect is created for paths that don't already have an extension.

It looks like the logic for checking whether a path already has an extension is inverted - paths WITHOUT extensions are being treated as if they already have one, so redirect rules aren't generated for them.

### Steps to reproduce
1. Configure the redirects plugin with `fromExtensions: ['html']`
2. Create a page at `/docs/intro`
3. Try to access `/docs/intro.html`
4. The redirect doesn't work - no redirect rule was created

### Expected behavior
- Paths without extensions should have redirect rules created
- Accessing `/docs/intro.html` should redirect to `/docs/intro`
- Paths that already end with `.html` (or other configured extensions) should be skipped

### Additional context
This seems to be affecting all extension-based redirects. The issue is that the condition for determining if a path already has an extension appears to be checking the wrong thing.

---
Repository: /testbed
