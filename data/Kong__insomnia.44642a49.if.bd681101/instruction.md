# Bug Report

### Describe the bug

I'm experiencing an issue with environment variable validation. When I try to save an environment with certain keys, the validation seems broken and I'm getting duplicate error messages or the app is behaving unexpectedly.

### Reproduction

I was editing my environment variables and noticed something strange happening. When I enter keys that should be validated, the behavior isn't consistent:

1. Create or edit an environment
2. Try adding a key that starts with `$` or contains `.`
3. The validation error appears but something seems off

I also noticed that if I look at the environment editor code, there appears to be duplicate function definitions which is causing weird behavior.

### Expected behavior

The environment key validation should work correctly without any duplicate code or unexpected behavior. Keys starting with `$` or containing `.` should be properly rejected with clear error messages.

### System Info
- Insomnia version: latest
- OS: N/A

This seems like it might be a merge conflict or refactoring issue that wasn't caught before being committed.

---
Repository: /testbed
