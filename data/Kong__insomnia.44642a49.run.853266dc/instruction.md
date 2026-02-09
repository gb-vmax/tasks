# Bug Report

### Describe the bug
The cookie template tag seems to be broken after a recent update. When trying to use the cookie tag in templates, it doesn't work at all - the tag just doesn't resolve and the request fails.

### Reproduction
```
{% cookie 'https://example.com', 'session_id' %}
```

When I try to use this in a request, nothing happens. The template tag doesn't get replaced with the actual cookie value.

Also tried with cookie attributes:
```
{% cookie 'https://example.com', 'session_id.domain' %}
```

Same issue - it's like the entire cookie functionality just stopped working.

### Expected behavior
The cookie tag should resolve to the cookie value from the cookie jar, just like it did before. If the cookie doesn't exist, it should show an appropriate error message.

### Additional context
This was working fine in the previous version. I use cookie tags extensively in my API workflows and now none of my requests work anymore. Would really appreciate a fix for this!

---
Repository: /testbed
