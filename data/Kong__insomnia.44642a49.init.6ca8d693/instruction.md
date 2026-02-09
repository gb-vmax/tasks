# Bug Report

### Describe the bug

When creating new environments, they appear in the wrong order in the UI. Instead of showing up at the top of the list as expected, newly created environments are appearing at the bottom.

### Reproduction

1. Open the application
2. Create a new environment
3. Observe where it appears in the environment list

The new environment shows up at the bottom instead of at the top of the list.

### Expected behavior

Newly created environments should appear at the top of the environment list, similar to how it worked in previous versions. The most recently created item should have the highest sort priority.

### Additional context

This seems to have started happening recently. The environment is created successfully and works fine, but the ordering is just backwards from what users would expect.

---
Repository: /testbed
