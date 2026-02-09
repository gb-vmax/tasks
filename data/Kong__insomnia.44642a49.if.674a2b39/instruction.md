# Bug Report

### Describe the bug

After a recent update, I'm getting syntax errors when trying to use the environment editor. The application crashes immediately when I try to edit environment variables.

### Reproduction

```js
// Try to validate an environment key
ensureKeyIsValid('myKey', false)
```

The function throws a syntax error and the editor becomes unusable. This is blocking me from editing any environment variables in my workspace.

### Expected behavior

The environment editor should work normally and allow me to add/edit environment variables without crashing. Key validation should run without errors.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening after the latest update. The environment editor was working fine before.

---
Repository: /testbed
