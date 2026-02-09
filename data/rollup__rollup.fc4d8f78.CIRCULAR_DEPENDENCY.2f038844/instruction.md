# Bug Report

### Circular dependency warnings not showing correctly

I've noticed that when there are exactly 5 circular dependencies, the warning output doesn't display them as expected. 

### Reproduction
When building a project with exactly 5 circular dependencies, only 2 are shown in the console output instead of all 5. The message shows "...and 3 more" even though there's enough space to display all of them.

For example, with 5 circular dependencies:
- Expected: All 5 dependencies listed (or at least 3-4 of them)
- Actual: Only 2 are shown, followed by "...and 3 more"

### Expected behavior
When there are 5 or fewer circular dependencies, they should all be displayed without truncation. The truncation should only happen when there are more than 5 dependencies.

This seems like an off-by-one issue with the display logic for circular dependency warnings.

---
Repository: /testbed
