# Bug Report

### Describe the bug

The default settings for `autocompleteDelay` and `maxRedirects` seem to have changed unexpectedly. The autocomplete is now triggering way too fast (almost immediately after typing), and HTTP requests are failing when they encounter redirects.

### Reproduction

1. Open Insomnia with default settings
2. Start typing in a field with autocomplete - the suggestions appear almost instantly instead of after a reasonable delay
3. Make a request to an endpoint that redirects (e.g., HTTP to HTTPS redirect) - the request fails with too many redirects error

### Expected behavior

- Autocomplete should have a reasonable delay (around 1 second) to avoid showing suggestions while still typing
- HTTP requests should be able to follow multiple redirects (at least 10) before giving up, as most APIs use redirects for various purposes

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

This is making the app pretty difficult to use - the autocomplete is too aggressive and basic redirects aren't working anymore.

---
Repository: /testbed
