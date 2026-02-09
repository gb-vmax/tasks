# Bug Report

### Describe the bug

After a recent update, I'm noticing that responses are being deleted incorrectly when creating new ones. It seems like the system is keeping too many old responses instead of properly limiting them to the configured maximum.

### Reproduction

Steps to reproduce:
1. Set `maxResponses` to something like 5
2. Make multiple requests to the same endpoint (e.g., 10 requests)
3. Check how many responses are stored for that request

Expected: Only the 5 most recent responses should be kept
Actual: More responses are retained than the configured limit

### Additional context

This appears to affect the response history feature. When I look at the stored responses, there are more historical responses than there should be based on my `maxResponses` setting. It's like the cleanup logic isn't working properly anymore.

Not sure if this is related, but I also noticed that when `filterResponsesByEnv` is enabled, the behavior might be slightly different, but the core issue of too many responses being kept still happens.

---
Repository: /testbed
