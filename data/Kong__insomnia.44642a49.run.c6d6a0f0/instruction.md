# Bug Report

### Describe the bug

I'm experiencing an issue with the `request` template tag where cookie retrieval appears to be broken. When trying to reference a cookie value using the template tag with the `cookie` attribute, it seems like the function is incomplete or not returning the expected result.

### Reproduction

```js
// In a request template
{% request 'cookie', 'sessionId' %}
```

When using the above template tag to retrieve a cookie named 'sessionId', the behavior is inconsistent or doesn't work at all. The cookie jar appears to be initialized correctly, but the actual cookie value is not being returned.

### Expected behavior

The template tag should:
1. Initialize the cookie jar for the workspace
2. Build the request URL with query parameters
3. Retrieve cookies matching the URL
4. Return the value of the specified cookie name

### Additional context

This appears to affect the `request` template tag specifically when using the `cookie` attribute. Other attributes like `url` seem to work fine. The issue might be related to how cookies are being processed or returned from the cookie jar.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
