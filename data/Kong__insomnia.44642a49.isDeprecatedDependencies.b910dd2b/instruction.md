# Bug Report

### Describe the bug

The plugin installation process is incorrectly flagging certain npm/yarn warnings as deprecation warnings when they shouldn't be. This causes legitimate warnings about dependencies to be silently ignored during plugin installation.

### Reproduction

When installing a plugin that has a warning message containing any one of these phrases:
- "no longer maintained"
- "not recommended for usage"  
- "upgrade your dependencies"

The warning is treated as a deprecation warning even if it's not actually about deprecated dependencies.

For example, a warning like:
```
Warning: This package is no longer maintained by the original author
```

Gets incorrectly classified as a deprecation warning and hidden from the user, even though it might be a critical security or compatibility warning.

### Expected behavior

The function should only treat a message as a deprecation warning when ALL of the following conditions are present:
- Contains "no longer maintained"
- Contains "not recommended for usage"
- Contains "upgrade your dependencies"

Currently it's treating messages as deprecation warnings if ANY of these phrases appear, which is too permissive and can hide important warnings from users.

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
