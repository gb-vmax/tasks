# Bug Report

### Describe the bug

After a recent update, importing Postman collections is completely broken. The importer crashes immediately when trying to process any collection file.

### Reproduction

1. Try to import any Postman collection (v2.1 format)
2. The import process fails to complete
3. No requests or folders are imported

I tested with multiple collection files that worked fine before, including simple collections with just a few requests and more complex ones with nested folders.

### Expected behavior

The Postman collection should import successfully, creating all requests and folders with their proper hierarchy and settings. Previously working collections should continue to work.

### System Info
- Insomnia version: latest
- OS: Windows 11

This is blocking our team from migrating collections. Any help would be appreciated!

---
Repository: /testbed
