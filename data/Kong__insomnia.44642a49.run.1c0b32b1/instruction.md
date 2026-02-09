# Bug Report

### Describe the bug

The cookie template tag is broken after a recent update. When trying to use `{% cookie 'url', 'cookieName' %}` in a request, it doesn't work at all and the template tag functionality appears to be incomplete.

### Reproduction

```
{% cookie 'https://example.com', 'session_id' %}
```

When I try to use the cookie tag in my requests, nothing happens. It looks like the code was refactored but not completed - the `run` function that actually executes the cookie lookup seems to have been removed and replaced with a helper function that's never called.

### Expected behavior

The cookie tag should:
1. Look up cookies from the workspace cookie jar
2. Find the cookie matching the specified name for the given URL
3. Return the cookie value

This was working fine before, but now it seems like the implementation is cut off mid-refactor.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
