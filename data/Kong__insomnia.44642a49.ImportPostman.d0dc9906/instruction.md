# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to import Postman collections. The import process fails completely and throws an error about unexpected token or incomplete code.

### Reproduction

Try to import any Postman collection (v2.1 format) using the import feature. The import fails immediately without processing any requests.

Steps:
1. Open the import dialog
2. Select a Postman collection file (JSON format)
3. Click import
4. The process fails with a syntax error

### Expected behavior

The Postman collection should import successfully, converting all requests, folders, and their configurations into the appropriate format. Both enabled and disabled items should be handled properly.

### Additional context

This seems to have broken recently. Previously, Postman collections were importing without any issues. The error appears to be related to the core import logic rather than the collection format itself, as even previously working collections now fail to import.

---
Repository: /testbed
