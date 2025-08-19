# Instructions to test `index.html`

Page directory

Home page - http://<addr>/
Chat view - http://<addr>/?api_key=<api_key>
Archive view - http://<addr>/?conversation_id=<conversation_id>

Navigation
- Home page will list some saved conversations
    - Clicking on the conversation will lead to the conversation view
- Archive view will display the conversation in full
    - Archive view will share the same elements
        - Instead of 
- Chat view has a button at the bottom where the user can save the current chat
    - This button is only visible on localhost


# Multi-chat view

Follow these instructions when you are done editing `index.html`.
If ANY of these fails, you HAVE to fix `index.html`.

What to do
- Open MCP Puppeteer with window size 1920 x 1000
- Run `echo $POE_API_KEY` to get the Poe API key to use
- Puppeteer execute `testRapidMessages()`
    - Take screenshots immediately and after 20 seconds
- Navigate between each response groups by clicking on the status message
    - Take a screenshot at every navigation


What to check (please make a TODO list and check off one-by-one)
- There should not be repeated user messages
- No user messages are dropped
- The user message and the status messages should interleave correctly
    - There should be one and only one status message for one user message
- All status messages should to navigate individual response groups
- Do not display success status messages when it hasn't succeeded
- Check the individual response groups
    - The responses should be different (since the questions are different) - especially for slow models
- Completions from the model should have the full context of the conversation
    - Please check the responses to "What is the sum from the last two answers?"
    - Each message must consider the preceeding conversation
    - Do not mix conversation threads - the conversation with each model should be isolated


```js
// Test script for rapid succession messages
// Run this in the browser console

function testRapidMessages() {
    const input = document.getElementById('messageInput');
    const button = document.getElementById('sendButton');
    
    // Send 3 "hi" messages with no delay between them
    for (let i = 0; i < 2; i++) {
        input.value = 'What is ' + i + ' to the power of ' + i + '? Use LaTeX and markdown.';
        button.click();
        console.log(`Sent message ${i + 1}`);
    }
    input.value = 'What is the sum from the last two answers?';
    button.click();
    console.log(`Sent final message`);
    
    console.log('Finished sending 3 messages rapidly');
}

// Run the test
testRapidMessages();
```

