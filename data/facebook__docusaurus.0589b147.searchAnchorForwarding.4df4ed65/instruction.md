# Bug Report

### Describe the bug

I'm experiencing an issue with client-side redirects where URLs with query parameters or hash fragments are not being forwarded correctly. It seems like the redirect logic is only working when BOTH search params AND hash are present, but it should work when either one exists.

### Reproduction

When setting up a redirect from an old URL to a new one:

```js
// Redirect configuration
{
  from: '/old-page',
  to: '/new-page?tab=overview'
}
```

Expected: Visiting `/old-page` should redirect to `/new-page?tab=overview` and preserve the query parameter.

Actual: The query parameter gets stripped during the redirect, and I end up at just `/new-page`.

Same issue happens with hash fragments:
```js
{
  from: '/old-docs',
  to: '/new-docs#getting-started'
}
```

The hash fragment is not being preserved during the redirect.

### Expected behavior

URLs with query parameters OR hash fragments should be properly forwarded during client-side redirects. The redirect mechanism should preserve these parts of the URL.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

This seems like it might be related to how the plugin determines whether to forward search/anchor information. Any help would be appreciated!

---
Repository: /testbed
