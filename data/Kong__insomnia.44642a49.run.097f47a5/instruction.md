# Bug Report

### Describe the bug

After a recent update, the cookie template tag is completely broken. When trying to reference cookies in requests using the `{% cookie %}` tag, the application crashes or fails to render the request properly.

### Reproduction

```js
// In a request, try to use the cookie template tag:
{% cookie 'https://example.com', 'session_id' %}
```

When this template tag is evaluated, the request fails to process. It looks like the code for handling cookies got corrupted or wasn't fully committed - the `run` function seems to be incomplete or missing entirely.

### Expected behavior

The cookie template tag should:
1. Extract cookies from the cookie jar for the given URL
2. Find the cookie with the specified name
3. Return the cookie value

Instead, the entire functionality appears to be broken.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

### Additional context

This seems like it might be related to a partial commit or merge conflict that wasn't fully resolved. The cookie handling code appears to have been replaced with incomplete helper functions (`extractDomainFromUrl`, `matchesDomain`) but the main `run` function is missing or cut off.

---
Repository: /testbed
