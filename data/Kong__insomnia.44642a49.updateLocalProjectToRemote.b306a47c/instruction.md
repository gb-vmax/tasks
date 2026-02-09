# Bug Report

### Describe the bug

After a recent update, I'm seeing duplicate code in the `updateLocalProjectToRemote` function in `project.ts`. It looks like the function body got duplicated somehow, with the entire logic block appearing twice in the same function. This causes the function to attempt creating a cloud project twice and handling the response incorrectly.

### Reproduction

Looking at the `updateLocalProjectToRemote` function in `packages/insomnia/src/models/helpers/project.ts`, you can see:

1. The function makes a POST request to create a new cloud project
2. Then it checks if there's an error and handles the response
3. But then the same POST request setup appears again with a different endpoint (`/team-projects` instead of `/projects`)

The function structure is malformed with the response handling logic appearing before the second request definition, which doesn't make sense logically.

### Expected behavior

The function should have a single, coherent flow:
1. Make one API request to create/update the cloud project
2. Handle the response appropriately
3. Update the local project with the remote ID
4. Return the result

The duplicate code block needs to be removed so the function works as intended.

### System Info
- Insomnia version: latest
- File: `packages/insomnia/src/models/helpers/project.ts`

---
Repository: /testbed
