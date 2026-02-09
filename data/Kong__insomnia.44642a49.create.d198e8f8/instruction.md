# Bug Report

### Describe the bug

I'm encountering an issue with settings initialization where the application fails to start properly. After a recent update, it seems like settings aren't being created or retrieved correctly, and the app gets stuck during initialization.

### Reproduction

The issue appears when:
1. Starting the application fresh (no existing settings)
2. The settings creation process is triggered
3. The app hangs or crashes because settings are null/undefined

I noticed this happens specifically during the initial setup flow when no settings document exists yet. The application expects a settings object but receives something unexpected.

### Expected behavior

The application should successfully create and retrieve settings on first launch, allowing the app to initialize properly. The settings object should be returned correctly from the creation process.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

This is blocking me from using the application at all since it won't get past the initialization stage. Any help would be appreciated!

---
Repository: /testbed
