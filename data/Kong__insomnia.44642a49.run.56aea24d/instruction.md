# Bug Report

### Describe the bug

The prompt template tag appears to be broken after a recent change. When trying to use the `{% prompt %}` tag in requests, it's not functioning at all - the tag doesn't render and requests fail to execute properly.

### Reproduction

1. Create a new request with a prompt tag in the URL or body:
```
GET https://api.example.com/users/{% prompt "User ID", "Enter user ID" %}
```

2. Send the request
3. The prompt dialog doesn't appear and the request fails

This also happens with more complex prompt configurations:
```
{% prompt "API Key", "Enter your API key", "", "my_api_key", true, true %}
```

### Expected behavior

The prompt dialog should appear when sending the request, allowing the user to enter a value. The entered value should be cached and used in the request.

### Additional context

This was working fine before. The prompt tag should:
- Show a dialog when the request is sent
- Cache values based on the storage key
- Support default values and masking text
- Return cached values when using explicit storage keys

Now it seems like the entire `run` function is missing or incomplete, causing the template tag to fail completely.

---
Repository: /testbed
