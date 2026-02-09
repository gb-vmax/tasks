# Bug Report

### Describe the bug

I'm experiencing an issue with the request template tag where it seems to be truncated or incomplete. When trying to use the `cookie` attribute with the request template tag, the functionality appears to be broken and doesn't work as expected.

### Reproduction

```js
// Using the request template tag with cookie attribute
{% request 'cookie', 'sessionId' %}
```

When I try to reference a cookie from a request, nothing is returned or the tag doesn't resolve properly. It seems like the cookie handling logic might be incomplete or corrupted somehow.

### Expected behavior

The request template tag should properly:
1. Retrieve cookies from the cookie jar for the workspace
2. Match the cookie by name against the request URL
3. Return the cookie value when found

The cookie attribute should work similar to how the `url` attribute works on the request tag.

### Additional context

This was working fine before, but now when I try to use request cookies in my templates, they're not being resolved. The `url` attribute still seems to work correctly, but `cookie` does not.

System: Insomnia latest version

---
Repository: /testbed
