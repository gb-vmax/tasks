# Bug Report

### Describe the bug

The prompt template tag appears to be broken after a recent update. When trying to use prompt tags in requests, I'm getting errors and the prompts are not showing up at all.

### Reproduction

```
Use a prompt tag in any request:
{% prompt "Enter API Key", "API Key", "default-value" %}
```

When sending the request, instead of showing a prompt dialog, the request fails or returns an empty/undefined value.

### Expected behavior

The prompt dialog should appear when sending a request with a prompt tag, allowing the user to enter a value. The tag should:
- Display the prompt with the specified title
- Use the provided label and default value
- Cache the value appropriately based on storage key settings
- Return the user-entered value

### Additional context

This was working fine before. The prompt tag is one of the core templating features and now it seems completely non-functional. Looking at the template tag definition, it seems like the `run` function might be incomplete or improperly defined.

---
Repository: /testbed
