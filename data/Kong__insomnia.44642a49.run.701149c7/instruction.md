# Bug Report

### Describe the bug

The cookie template tag appears to be broken after a recent update. When trying to use the `{% cookie %}` tag to retrieve cookie values, I'm getting errors or the tag doesn't work at all.

### Reproduction

I have a simple template that tries to get a cookie value:

```
{% cookie 'https://example.com', 'sessionId' %}
```

Previously this worked fine and returned the cookie value, but now it seems like the functionality is completely broken. The request fails to send and I can't access any cookie values through templating anymore.

### Expected behavior

The cookie tag should retrieve the cookie value for the specified URL and cookie name, just like it did before. It should return the cookie value that's stored in the cookie jar for the workspace.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my workflow as I rely heavily on cookie templating for authentication flows. Any help would be appreciated!

---
Repository: /testbed
