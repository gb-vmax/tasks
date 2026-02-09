# Bug Report

### Describe the bug

I'm experiencing an issue with client redirects where the redirect page is not properly forwarding query parameters and hash anchors to the target URL. After a recent update, redirects seem to only work for the base URL but ignore any search params or anchors that should be preserved during the redirect.

### Reproduction

1. Set up a redirect from `/old-page` to `/new-page`
2. Navigate to `/old-page?foo=bar#section`
3. The redirect goes to `/new-page` instead of `/new-page?foo=bar#section`

Expected: Query parameters and hash anchors should be forwarded to the target URL during redirect.

Actual: Only the base target URL is used, losing any query params and anchors.

This is breaking our documentation links that rely on deep linking with anchors and query parameters. The redirect page seems to be missing some data that was previously available.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

---
Repository: /testbed
