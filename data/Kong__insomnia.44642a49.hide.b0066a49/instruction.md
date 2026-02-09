# Bug Report

### Describe the bug

The JSONPath Filter field in the OS template tag is not showing/hiding correctly based on the selected OS function. The visibility logic appears to be inverted or broken - the filter field is hidden when it should be shown and vice versa.

### Reproduction

1. Open a request in Insomnia
2. Add an OS template tag
3. Select `userInfo` or `cpus` as the OS function
4. The JSONPath Filter field should appear (since these functions return objects that can be filtered)
5. Instead, the field is hidden or behaves unexpectedly

Alternatively:
1. Select an OS function that doesn't return objects (like `platform` or `arch`)
2. The JSONPath Filter field should be hidden
3. The field may be showing when it shouldn't

### Expected behavior

The JSONPath Filter field should only be visible when selecting OS functions that return objects (`userInfo` or `cpus`). For other OS functions that return simple values, the filter field should be hidden since there's nothing to filter.

### System Info
- Insomnia version: latest
- OS: Various

---
Repository: /testbed
