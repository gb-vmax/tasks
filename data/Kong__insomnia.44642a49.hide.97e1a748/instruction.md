# Bug Report

### Describe the bug

I'm experiencing an issue with the template tag UI where the "Max age (seconds)" field visibility behavior has changed unexpectedly. The field now shows up in cases where it shouldn't be visible, and hides in cases where it should be shown.

### Reproduction

When configuring a template tag with trigger behavior settings:

1. Set the trigger behavior to "when-expired"
2. The "Max age (seconds)" field is now hidden (but it should be visible)
3. Set the trigger behavior to "always"  
4. The "Max age (seconds)" field remains hidden (but it should also be visible for this option)
5. Set the trigger behavior to "never" or "no-history"
6. The field correctly stays hidden

It seems like the logic for when to show/hide the max age field got inverted or changed. Previously, the max age field would only appear when the trigger behavior was set to "when-expired", but now it's doing the opposite.

### Expected behavior

The "Max age (seconds)" field should be visible when trigger behavior is set to "when-expired" or "always", since these are the modes where caching with expiration makes sense. It should be hidden for "never" and "no-history" modes.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
