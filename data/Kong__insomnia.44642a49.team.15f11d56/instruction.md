# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the sync functionality. The application fails to start and throws an error about an unexpected token in the type-schemas file.

### Reproduction

Just trying to start the application normally. The error appears immediately on startup:

```
SyntaxError: Unexpected token 'let'
```

The error is coming from `packages/insomnia/src/sync/__schemas__/type-schemas.ts` in the `backendProjectWithTeamSchema` definition.

### Expected behavior

The application should start without syntax errors. The schema definitions should be properly formatted and parseable.

### System Info
- Insomnia version: latest
- OS: macOS

Not sure what changed but this is blocking me from using the app at all. Any help would be appreciated!

---
Repository: /testbed
