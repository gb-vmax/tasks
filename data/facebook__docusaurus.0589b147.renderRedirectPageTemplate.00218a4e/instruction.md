# Bug Report

### Describe the bug

I'm experiencing an issue with the client redirects plugin where the search and anchor forwarding behavior appears to be inverted. When I configure a redirect with `searchAnchorForwarding: true`, the search parameters and anchors are NOT being forwarded to the destination URL. Conversely, when set to `false`, they ARE being forwarded.

### Reproduction

Set up a redirect configuration:

```js
{
  from: '/old-page',
  to: '/new-page',
  searchAnchorForwarding: true
}
```

Then navigate to: `/old-page?foo=bar#section`

**Expected:** Should redirect to `/new-page?foo=bar#section`
**Actual:** Redirects to `/new-page` (without search params and anchor)

If I change `searchAnchorForwarding: false`, then the search params and anchor ARE included in the redirect, which is the opposite of what I would expect.

### Expected behavior

When `searchAnchorForwarding` is set to `true`, the redirect should preserve query parameters and URL fragments/anchors from the source URL to the destination URL.

When set to `false`, these should be stripped.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
