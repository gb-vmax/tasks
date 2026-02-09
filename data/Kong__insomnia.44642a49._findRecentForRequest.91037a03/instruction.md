# Bug Report

### Describe the bug

I'm experiencing an issue where response history is being deleted incorrectly. When making requests, all my previous responses are getting removed instead of keeping the most recent ones up to the configured limit.

### Reproduction

1. Set max responses to keep to 20 in settings
2. Make a request to an endpoint
3. Make the same request again
4. Check the response history

Expected: Should keep up to 20 most recent responses
Actual: All previous responses are deleted, only the newest one remains

### Additional context

This seems to have started recently. I rely on being able to compare responses over time, but now I can only see the very last response made. The response history is essentially unusable now.

Also noticed that when I have "Filter responses by environment" enabled, responses from other environments are showing up in the history, which shouldn't happen.

---
Repository: /testbed
