# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with branch caching during project pulls. The cache doesn't seem to be getting cleared properly between different projects, causing stale branch data to be returned.

### Reproduction

When pulling multiple backend projects in sequence, the second project sometimes returns the branch list from the first project instead of fetching its own branches.

Steps to reproduce:
1. Pull a backend project (e.g., project A with branches: main, feature-1)
2. Immediately pull a different backend project (e.g., project B with branches: main, feature-2)
3. Project B incorrectly shows branches from project A

The cache key appears to be constructed using `backendProject.id`, but it seems like the cache is persisting across different pull operations when it shouldn't.

### Expected behavior

Each project should fetch and cache its own set of remote branches independently. The cache should be isolated per project and not leak data between different backend projects.

### Additional context

This is causing issues in our workflow where we need to sync multiple projects back-to-back. The workaround right now is to add delays between pulls, but that's not ideal.

---
Repository: /testbed
