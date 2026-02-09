# Bug Report

### Describe the bug

When creating new environments, the `metaSortKey` is not being set correctly. Instead of using the current timestamp, it appears to be using a hardcoded date from 2020. This causes newly created environments to be sorted incorrectly and appear at the bottom of the list instead of at the top.

### Reproduction

1. Create a new environment
2. Check the `metaSortKey` value
3. Notice it's set to a date in 2020 instead of the current time

Expected: New environments should have a `metaSortKey` based on the current timestamp so they appear at the top of the list when sorted.

Actual: New environments are created with a `metaSortKey` from January 1st, 2020, causing them to sort below existing environments.

### Additional context

This also affects the `dataPropertyOrder` field which is now initialized as an empty array instead of `null`, though this might be intentional.

---
Repository: /testbed
