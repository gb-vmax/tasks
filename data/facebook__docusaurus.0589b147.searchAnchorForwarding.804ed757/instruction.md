# Bug Report

### Describe the bug

I'm experiencing an issue with client-side redirects where search parameters and URL anchors/fragments are not being forwarded correctly to the destination URL.

When I set up a redirect from one page to another, if the source URL contains query parameters (like `?foo=bar`) OR a hash fragment (like `#section`), they should be preserved and forwarded to the destination URL. However, this doesn't seem to be working as expected.

### Reproduction

Set up a redirect in your Docusaurus config:

```js
redirects: [
  {
    from: '/old-page',
    to: '/new-page',
  },
]
```

Then try accessing:
- `/old-page?search=test` - the `?search=test` is not forwarded to `/new-page`
- `/old-page#anchor` - the `#anchor` is not forwarded to `/new-page`

### Expected behavior

When navigating to `/old-page?search=test`, I should be redirected to `/new-page?search=test` with the search parameters preserved.

Similarly, when navigating to `/old-page#anchor`, I should be redirected to `/new-page#anchor` with the hash fragment preserved.

This is important for maintaining deep links and ensuring users land on the correct section of the new page.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
