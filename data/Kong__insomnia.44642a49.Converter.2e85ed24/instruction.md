# Bug Report

### Describe the bug

After a recent update, I'm getting errors when trying to import Postman collections. The import process fails with a "calculateCollect is not defined" error. This appears to be breaking all Postman collection imports.

### Reproduction

1. Try to import any valid Postman collection file
2. The import process starts but fails immediately
3. Error message indicates an undefined function

This is blocking our ability to import any Postman collections into Insomnia. The issue seems to have been introduced in a recent change to the Postman importer.

### Expected behavior

Postman collections should import successfully without errors. The importer should process the collection and create the appropriate requests and folders.

### System Info
- Insomnia version: Latest
- OS: Multiple (reproduced on Windows and macOS)

---
Repository: /testbed
