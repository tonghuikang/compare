Serving
- Puppeteer navigate to `http://localhost:64088/`
- `./start_server.sh`


Testing
- Any changes to `index.html` should be tested with Puppeteer
- Run `echo $POE_API_KEY` to get the Poe API key to use
- Puppeteer execute `testRapidMessages()`
    - Take screenshots immediately and 5 seconds later
- What to check (please make a TODO list and check off one-by-one)
    - There should not be repeated user messages
    - The user message and the status messages should interleave correctly
        - There should be one and only one status message for one user message
    - No user messages are dropped
    - All status messages should to navigate individual response groups
    - Do not display success status messages when it hasn't succeeded
    - Check the individual response groups
        - The responses should be different (since the questions are different) - especially for slow models
    - Completions from the model should have the full context of the conversation
    - Slow responses should not block successive user messages from being processed

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



Warnings
- Do not put any API keys in code
