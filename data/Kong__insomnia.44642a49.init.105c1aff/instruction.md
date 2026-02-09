# Bug Report

### Describe the bug

After a recent update, creating new proto files is generating duplicate names instead of incrementing properly. When you create multiple proto files, they all end up with the same name or incorrect numbering.

### Reproduction

Steps to reproduce:
1. Create a new proto file (should be named "New Proto File")
2. Create another proto file (should be named "New Proto File 2")
3. Create a third proto file (should be named "New Proto File 3")

What actually happens:
- The naming sequence gets messed up
- Files might get numbered incorrectly or have duplicate names
- The unique name generation doesn't seem to be working as expected

### Expected behavior

Each new proto file should get a unique name with proper incrementing:
- First file: "New Proto File"
- Second file: "New Proto File 2"
- Third file: "New Proto File 3"
- And so on...

The numbering should continue sequentially even if files are deleted in between.

### Additional context

This seems to have started happening recently. The proto files are also being created with a default template now instead of being empty, which is nice, but the naming issue is causing problems when managing multiple proto files in a project.

---
Repository: /testbed
