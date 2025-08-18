Serving
- Puppeteer navigate to `http://localhost:64088/`
- `./start_server.sh`


Testing
- Any changes to `index.html` should be tested with Puppeteer
- Run `echo $POE_API_KEY` to get the Poe API key to use
- Puppeteer execute `testRapidMessages()`
    - Take screenshots immediately and 5 seconds later
- What to check
    - There should not be repeated user messages
    - The user message and the status messages should interleave correctly
    - No user messages are dropped
    - All status messages should to navigate individual response groups
    - Do not display success status messages when it hasn't succeeded
    - Check the individual response groups
        - The responses should be different (since the questions are different) - especially for slow models

```js
// Test script for rapid succession messages
// Run this in the browser console

function testRapidMessages() {
    const input = document.getElementById('messageInput');
    const button = document.getElementById('sendButton');
    
    // Send 3 "hi" messages with no delay between them
    for (let i = 0; i < 3; i++) {
        input.value = 'What is ' + i + ' to the power of ' + i;
        button.click();
        console.log(`Sent message ${i + 1}`);
    }
    
    console.log('Finished sending 3 messages rapidly');
}

// Run the test
testRapidMessages();
``



Warnings
- Put any API keys in code
