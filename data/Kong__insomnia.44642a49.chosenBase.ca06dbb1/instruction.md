# Bug Report

### Describe the bug

After a recent update, the application crashes during startup when trying to repair/migrate workspace data. The app becomes completely unusable and won't load any workspaces.

### Reproduction

1. Start the application with existing workspace data that has multiple base environments or cookie jars
2. Application attempts to run database repair functions during initialization
3. App crashes with a syntax error

This seems to be affecting the database migration/repair logic. The issue occurs consistently on startup and prevents the application from loading.

### Expected behavior

The application should start normally and successfully repair any database inconsistencies (like merging duplicate base environments or cookie jars) without crashing.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
