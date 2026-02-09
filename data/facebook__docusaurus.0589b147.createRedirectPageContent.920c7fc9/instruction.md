# Bug Report

### Describe the bug

I'm experiencing an issue with client-side redirects where URLs containing special characters are not being encoded properly. When redirecting to a URL with characters that need URL encoding, the redirect page fails to work correctly.

### Reproduction

```js
// When creating a redirect to a URL with special characters
const redirectConfig = {
  from: '/old-page',
  to: '/new-page?query=hello world&foo=bar'
}

// The generated redirect page doesn't properly handle the URL encoding
// The spaces and special characters in the query parameters cause issues
```

### Expected behavior

URLs with special characters (spaces, ampersands, etc.) should be properly encoded when generating redirect pages. The redirect should work seamlessly regardless of the characters present in the target URL.

### Additional context

This affects redirects that include:
- Query parameters with spaces or special characters
- Hash fragments with encoded characters
- Any URL that requires encoding

The redirect page generation seems to not be handling URL encoding consistently, which breaks the redirect functionality for these cases.

---
Repository: /testbed
