# Bug Report

### Describe the bug

I'm experiencing an issue with docs plugin routing where nested documentation paths are not being matched correctly. When I navigate to a nested doc path, it's not finding the correct plugin instance.

### Reproduction

Setup:
- Multiple docs plugin instances with different base paths
- One plugin at `/` (root)
- Another plugin at `/android`

Steps to reproduce:
1. Configure two docs plugins, one with path `/` and one with path `/android`
2. Navigate to `/android/foo` (a page under the android docs)
3. The page doesn't load or matches the wrong plugin instance

Expected: Should match the `/android` plugin instance
Actual: Seems to be matching the root `/` plugin instead

### Additional context

This seems to affect any setup where you have a root-level docs plugin alongside other plugins with specific base paths. The routing logic doesn't appear to be prioritizing more specific paths over general ones.

---
Repository: /testbed
