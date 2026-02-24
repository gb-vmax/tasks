You are an automation specialist organizing workflow configurations. Under your home folder, there is a YAML file at <code>/home/user/workflows/build.yml</code> with several steps for a CI pipeline. 

Please do the following:

- Add a new step to the end of the existing steps sequence in the YAML file.
- The new step must have the following structure and indentation, matching the style of the file:
  <pre>
    - name: deploy
      run: ./deploy.sh
  </pre>
- The final file must remain valid YAML and preserve any existing formatting or structure—do not alter any other content except for appending this step.
- After editing, create a plain text log file at <code>/home/user/workflows/edit.log</code> containing only this line (no extra whitespace or newlines):
  <pre>
  Step 'deploy' added to build.yml
  </pre>

The automated test will check both that the new step is appended correctly (with exact keys and ordering), and that <code>edit.log</code> contains exactly the specified message with no extra lines or characters.
