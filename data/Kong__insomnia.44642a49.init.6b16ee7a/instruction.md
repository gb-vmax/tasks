# Bug Report

### Describe the bug

When creating multiple proto files in succession, they all get the same name "New Proto File" instead of having unique names. This makes it confusing to distinguish between different proto files in the UI.

### Reproduction

1. Create a new proto file - it gets named "New Proto File"
2. Create another proto file - it also gets named "New Proto File" (should be "New Proto File 2")
3. Create a third proto file - still named "New Proto File" (should be "New Proto File 3")

All files end up with identical names, making it hard to tell them apart.

### Expected behavior

Each new proto file should automatically get a unique name:
- First file: "New Proto File"
- Second file: "New Proto File 2"
- Third file: "New Proto File 3"
- And so on...

Similar to how other apps handle duplicate names (like "Untitled", "Untitled 2", etc.)

### Additional context

Also noticed that the first proto file I create is empty, but I expected it to have some kind of starter template or example code to help me get started. Would be nice if at least the first file had a basic proto3 example.

---
Repository: /testbed
