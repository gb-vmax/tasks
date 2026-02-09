# Bug Report

### Describe the bug

When loading application settings, the wrong settings object is being returned in certain scenarios. After restarting the application or in situations where settings already exist, the application appears to either create duplicate settings or retrieve the incorrect settings instance.

### Reproduction

1. Launch the application for the first time (settings should be created)
2. Modify some settings and save them
3. Restart the application
4. The settings appear to be reset or different from what was saved

Alternatively, if multiple settings objects exist in the database:
1. The application retrieves the second settings object instead of the first one
2. This causes unexpected behavior where settings changes don't persist correctly

### Expected behavior

The application should consistently retrieve the first (and ideally only) settings object from the database. If no settings exist, it should create a new one. The same settings instance should be used throughout the application lifecycle.

### Additional context

This seems to be related to how settings are loaded from the database. The logic for determining when to create new settings vs. retrieving existing ones may be inverted.

---
Repository: /testbed
