# Bug Report

### Describe the bug

The prompt template tag appears to be broken after a recent change. When I try to use it in my requests, nothing happens and the prompt doesn't show up at all. The template tag just seems to be incomplete or cut off.

### Reproduction

I have a request with a prompt tag like this:

```
{% prompt 'API Key', 'Enter your API key', '', 'api_key_storage' %}
```

When I try to send the request, the prompt dialog doesn't appear and the tag doesn't render any value. It seems like the functionality is just missing.

### Expected behavior

The prompt dialog should appear when sending the request, allowing me to enter a value. The entered value should be cached using the storage key and returned as the tag's value.

### Additional context

This was working fine before. I'm using the prompt tag with a storage key to cache API keys between requests. Now the entire prompt functionality seems to be gone.

---
Repository: /testbed
