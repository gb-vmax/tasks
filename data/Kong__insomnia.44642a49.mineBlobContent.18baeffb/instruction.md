# Bug Report

### Describe the bug

The merge conflict schema appears to have a syntax error that prevents the application from starting. When trying to load the sync module, I'm getting parsing errors related to the schema definition.

### Reproduction

1. Start the application after the recent changes to `type-schemas.ts`
2. Try to access any sync-related functionality
3. Application fails to load properly

It looks like there's an issue with how the `mineBlobContent` property is defined in the `mergeConflictSchema` object. The code structure seems malformed with function definitions appearing where they shouldn't be.

### Expected behavior

The application should start normally and the merge conflict schema should be properly defined without syntax errors.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
