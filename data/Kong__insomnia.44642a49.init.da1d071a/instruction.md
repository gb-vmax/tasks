# Bug Report

### Describe the bug

When creating multiple unit test suites with the same base name, the sort order becomes inconsistent and suites don't appear in the expected order. Instead of new duplicate suites being placed near their related suites, they appear at seemingly random positions in the list.

### Reproduction

1. Create a new unit test suite (it gets named "My Test")
2. Create another unit test suite (should be named "My Test 2")
3. Create a third unit test suite (should be named "My Test 3")
4. Observe the ordering in the suite list

### Expected behavior

New test suites with similar names should be grouped together and maintain a predictable sort order. When I create "My Test 2", it should appear right after "My Test", and "My Test 3" should appear after "My Test 2".

### Actual behavior

The suites appear in an unexpected order. Sometimes newer suites appear before older ones, and the ordering doesn't follow any clear pattern.

### System Info
- Insomnia version: latest
- OS: macOS

This is making it difficult to organize test suites when I have multiple suites with similar names. Would appreciate any help with this!

---
Repository: /testbed
