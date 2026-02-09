# Bug Report

### Describe the bug

When installing plugins with deprecated dependencies, Insomnia is incorrectly filtering out deprecation warnings. Some valid deprecation warnings are being treated as false positives and suppressed, while others that should be filtered are not being caught properly.

### Reproduction

1. Install a plugin that has deprecated dependencies with warnings like:
   - "package X is no longer maintained"
   - "package Y is not recommended for usage"
   - "package Z is deprecated, please upgrade your dependencies"

2. Observe which deprecation warnings are shown vs. hidden

### Expected behavior

The deprecation warning filter should correctly identify all standard yarn deprecation messages and handle them consistently. Currently the logic seems to be backwards - warnings that should be filtered are shown, and some that should be shown are filtered.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
