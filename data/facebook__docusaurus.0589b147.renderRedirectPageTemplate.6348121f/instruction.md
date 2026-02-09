# Bug Report

### Describe the bug

After a recent update, redirect pages are not working correctly. The redirect metadata like `delay` and `searchAnchorForwarding` seems to be ignored, and only the `toUrl` is being used. This breaks the redirect behavior for pages that need custom delay times or anchor forwarding.

### Reproduction

```js
// Create a redirect with custom settings
const redirectData = {
  toUrl: '/new-page',
  delay: 5,
  searchAnchorForwarding: true
}

// Generate redirect page
const pageContent = renderRedirectPageTemplate(redirectData)

// The generated page only uses toUrl, ignoring delay and searchAnchorForwarding
```

### Expected behavior

The redirect page should respect all provided configuration options including:
- `toUrl` - the destination URL
- `delay` - custom delay before redirect
- `searchAnchorForwarding` - whether to forward URL anchors and search params

All these properties should be passed to the template and rendered in the final redirect page HTML.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

---
Repository: /testbed
