# Bug Report

### Describe the bug

When using client redirects with URLs containing special characters, the redirect page is not being generated correctly. The `toUrl` in the redirect template appears to be unencoded, which can cause issues with certain URL characters.

### Reproduction

```js
// Create a redirect with special characters in the URL
{
  from: '/old-path',
  to: '/new-path/with spaces/and#anchor'
}
```

When the redirect page is created, the URL special characters are not properly encoded in the template, but the search/anchor forwarding logic is receiving an unencoded URL.

### Expected behavior

The redirect URL should be properly encoded when passed to the template, while the search/anchor forwarding should work with the encoded version to ensure consistent URL handling.

### System Info
- Docusaurus plugin: client-redirects
- Version: latest

---
Repository: /testbed
