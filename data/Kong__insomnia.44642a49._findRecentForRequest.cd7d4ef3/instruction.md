# Bug Report

### Describe the bug

After a recent update, responses are not being created properly. When trying to send requests, the application appears to hang or fail silently without creating response records in the database.

### Reproduction

1. Open Insomnia
2. Create a new request (any type - GET, POST, etc.)
3. Try to send the request
4. The request appears to process but no response is saved/displayed

It seems like the response creation logic got interrupted or broken. The `create` function for responses appears to be incomplete - it starts setting up the request version but doesn't actually finish creating the response object.

### Expected behavior

Requests should complete successfully and response data should be stored and displayed in the UI. The response creation should:
- Create a proper Response object
- Store it in the database
- Return the created response

### System Info
- Insomnia version: Latest
- OS: Multiple (reproduced on macOS and Windows)

This is blocking all API testing work since we can't see any response data anymore. Any help would be greatly appreciated!

---
Repository: /testbed
