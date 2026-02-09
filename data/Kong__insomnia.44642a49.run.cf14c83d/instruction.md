# Bug Report

### Describe the bug

The prompt template tag appears to be broken after a recent change. When trying to use prompts in requests, the application throws an error and the prompt functionality doesn't work at all.

### Reproduction

```js
// Using a prompt tag in a request
{% prompt "Enter API Key", "API Key", "default-value" %}
```

When sending a request with this prompt tag, instead of showing the prompt dialog, the application crashes or doesn't render the prompt correctly.

### Expected behavior

The prompt should display a dialog asking for user input with the specified title and label, and return the entered value (or cached value if available). The prompt should support features like:
- Caching values based on storage keys
- Using last saved values as defaults
- Masking text for password inputs
- Only prompting during actual request sends

### Additional context

This seems to have started happening recently. The prompt tag was working fine before, but now it's completely non-functional. It looks like the code might be incomplete or corrupted somehow - the function definition appears to be cut off or replaced with something else.

---
Repository: /testbed
