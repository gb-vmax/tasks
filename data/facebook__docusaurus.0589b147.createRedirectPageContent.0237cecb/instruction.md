# Bug Report

### Describe the bug

I'm experiencing an issue with URL redirects where URLs containing certain special characters are being double-encoded, resulting in broken redirect links. When a redirect is created with a URL that has characters like spaces or other special characters, the final URL becomes malformed.

### Reproduction

When creating a redirect to a URL with special characters, the redirect page generates an incorrectly encoded URL. For example:

```
Original URL: /docs/my page/guide
Expected redirect URL: /docs/my%20page/guide
Actual redirect URL: /docs/my%2520page/guide
```

The URL appears to be encoded twice, causing the redirect to fail or point to the wrong location.

### Expected behavior

URLs should only be encoded once. A redirect to `/docs/my page/guide` should result in `/docs/my%20page/guide`, not `/docs/my%2520page/guide`.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

---
Repository: /testbed
