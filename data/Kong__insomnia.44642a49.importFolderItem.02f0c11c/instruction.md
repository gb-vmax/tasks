# Bug Report

### Describe the bug
When importing Postman collections with folders that have descriptions, the authentication settings are being replaced with the `afterResponseScript` value instead of the actual authentication data. This causes requests within those folders to lose their authentication configuration.

### Reproduction
1. Create a Postman collection with a folder that has:
   - A description field set
   - Authentication configured (e.g., Bearer token, API key, etc.)
2. Export the collection from Postman
3. Import the collection into Insomnia
4. Check the folder's authentication settings

The authentication will be set to the after-response script value instead of the actual auth configuration.

### Expected behavior
The folder should retain its authentication settings regardless of whether it has a description or not. The authentication field should always contain the imported authentication data.

### Additional context
This appears to affect any folder with a description field. Folders without descriptions seem to import correctly with their authentication intact.

---
Repository: /testbed
