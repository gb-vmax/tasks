# Bug Report

### Describe the bug

After a recent update, I'm noticing that the default timeout value seems to have changed dramatically. Requests are now timing out almost immediately instead of waiting the expected amount of time.

### Reproduction

1. Create a new request to any endpoint that takes more than a few seconds to respond
2. Send the request without modifying any timeout settings
3. The request times out after only 30 milliseconds instead of the expected 30 seconds

### Expected behavior

New installations should have a default timeout of 30 seconds (30000 milliseconds), not 30 milliseconds. This makes the app essentially unusable for any API that takes more than a trivial amount of time to respond.

### Additional context

This appears to affect fresh installations where settings haven't been customized yet. Also noticed that `autoDetectColorScheme` is now enabled by default when it wasn't before, though that's less critical.

---
Repository: /testbed
