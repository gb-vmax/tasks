# Bug Report

### Describe the bug

After a recent update, newly created Proto Files are getting auto-generated names with timestamps instead of the simple "New Proto File" name, and they come pre-filled with default proto3 template content. This is breaking our workflow where we expect empty proto files with consistent naming.

### Reproduction

1. Create a new Proto File in the application
2. Observe the name - it will be something like "New Proto File 1234" (with a number based on timestamp)
3. Check the content - it contains a pre-filled proto3 message template instead of being empty

### Expected behavior

- New Proto Files should be named "New Proto File" (without any timestamp suffix)
- The protoText field should be empty by default, allowing users to start with a blank slate

This is causing issues in our automated tests and scripts that rely on the consistent "New Proto File" naming convention. The auto-generated template is also unexpected since we have our own templates we prefer to use.

---
Repository: /testbed
