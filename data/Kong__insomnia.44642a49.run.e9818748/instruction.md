# Bug Report

### Describe the bug

The prompt template tag appears to be broken after a recent change. When I try to use it in my requests, nothing happens and the values aren't being rendered properly. It looks like the entire `run` function implementation was removed or corrupted.

### Reproduction

```js
// Using a prompt tag in a request
{% prompt "API Key", "Enter your API key", "", "api_key_storage" %}
```

When I try to send a request with this template tag, it doesn't prompt me for input and the value is not being substituted. The template just doesn't work at all.

### Expected behavior

The prompt should:
1. Display a dialog asking for user input with the specified title
2. Use the cached value if available and explicitly defined storage key is provided
3. Save the value to storage under the specified key
4. Return the entered value to be used in the request

### Additional context

This was working fine before, but now it seems like the core functionality of the prompt tag has been completely removed. The `run` function that handles prompting, caching, and storage appears to be missing or incomplete.

---
Repository: /testbed
