# Bug Report

### Describe the bug

The name sorting behavior seems broken after a recent update. When sorting items alphabetically, items that start with the same letter are not being ordered correctly. For example, if I have requests named "aTest", "anotherTest", and "apple", they don't sort in the expected alphabetical order.

### Reproduction

Create multiple requests/folders with names that share common prefixes:
- "aTest"
- "anotherTest" 
- "apple"
- "application"

When sorted alphabetically (ascending), the order appears incorrect - items aren't following standard alphabetical sorting rules.

### Expected behavior

Items should be sorted in proper alphabetical order using standard locale comparison. "aTest" should come before "anotherTest", which should come before "apple", etc.

The sorting was working fine in previous versions but now produces unexpected results.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
