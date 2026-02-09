# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with pulling backend projects. The application seems to hang or take an extremely long time when trying to fetch remote branches. Sometimes it eventually completes, but other times it just times out completely.

### Reproduction

1. Try to pull a backend project with remote branches
2. The pull operation gets stuck during the remote branch fetching phase
3. Application becomes unresponsive or takes significantly longer than before

### Expected behavior

The pull operation should complete quickly and reliably like it did in previous versions. Remote branches should be fetched without delays or hanging.

### Additional context

This seems to have started happening after the latest changes to the pull backend project functionality. The issue is intermittent - sometimes it works fine, other times it completely hangs. When it does work, it's noticeably slower than before.

---
Repository: /testbed
