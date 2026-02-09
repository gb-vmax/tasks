# Bug Report

### Describe the bug

I'm encountering a syntax error in the database module that's preventing the application from starting. It looks like there's a duplicate function declaration for the `remove` method in the database object.

### Reproduction

When trying to start the application after the latest update, I get a parsing error. The `database.ts` file has what appears to be duplicate code in the `remove` function - the function signature appears twice at lines 445 and 446.

```typescript
remove: async function<T extends BaseModel>(doc: T, fromSync = false) {
 remove: async function<T extends BaseModel>(doc: T, fromSync = false) {
```

This causes the application to fail during the build/transpilation phase.

### Expected behavior

The database module should compile successfully and the application should start without syntax errors.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
