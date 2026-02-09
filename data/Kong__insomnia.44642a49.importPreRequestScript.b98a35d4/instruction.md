# Bug Report

### Describe the bug

When importing Postman collections, pre-request scripts are not being imported correctly. The scripts that should run before a request is sent are not showing up in the imported requests.

### Reproduction

1. Create a Postman collection with a request that has a pre-request script
2. Add some script code in the "Pre-request Script" tab in Postman (e.g., `pm.environment.set("test", "value")`)
3. Export the collection from Postman
4. Import the collection into Insomnia
5. Check the imported request

### Expected behavior

The pre-request script from Postman should be imported and available in the imported request. Instead, the pre-request script section is empty after import.

### Additional context

This seems to have broken recently. I have several Postman collections with pre-request scripts that I need to migrate, but they're all coming in without the scripts attached.

---
Repository: /testbed
