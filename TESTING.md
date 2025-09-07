# Instructions to test `index.html`

Page directory

Home page - http://<addr>/
Chat view - http://<addr>/?api_key=<api_key>
Archive view - http://<addr>/?conversation_id=<conversation_id>

Navigation
- Home page displays a box where you can pass your API key to start a chat, or list some saved conversations
    - Putting your API key will lead you to the chat view
    - Clicking on the conversation will lead to the conversation view
        - Only the title is displayed at the conversation home page
- Chat view will allow the user to talk to all the models
    - There is a green button at the bottom right where the user can save the current chat
        - This button is only visible on localhost
        - The button does not work if the conversation is empty
        - (Please git reset the files after testing them)
- Archive view will display the conversation in full
    - Archive view will share the same elements with chat view
        - Instead of the ask bar, the description (from comparison_registry.json) will be displayed instead
        - The "Start New Chat →" button will show a modal asking for API key
            - The modal will indicate if the conversation will be imported
            - After entering API key, it navigates to chat view with imported messages
                - The imported message should include both user and assistant messages



# Testing the home page

Follow these instructions when you are done working on the chat view in `index.html`.
If ANY of these fails, you HAVE to fix `index.html`.

What to do
- Open MCP Puppeteer with window size 1920 x 1000
- Run `echo $POE_API_KEY` to get the Poe API key to use

What to check (please make a TODO list and check off one-by-one)
- Navigating to the chat view by providing an API key works
- Navigating to the archive view by clicking on a conversation works



# Testing the chat view

Follow these instructions when you are done working on the chat view in `index.html`.
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
    - There should be one and only one status message for each user message, interleaved
- All status messages should to navigate individual response groups
- Do not process future messages for a bot if a previous message for a bot has yet to be processed
- Do not display success status messages when it hasn't succeeded
- Iterate over ALL the individual response groups
    - The responses should be different (since the questions are different)
    - Completions from the model should have the full context of the conversation
        - Each message must consider the preceeding conversation
            - The responses from previous questions should be passed as input
        - Each model should maintain its own conversation thread


```js
// Test script for rapid succession messages
// Run this in the browser console

async function testRapidMessages() {
    const input = document.getElementById('messageInput');
    const button = document.getElementById('sendButton');
    
    // Helper function to wait
    const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
    
    // Send messages with delay between them
    for (let i = 0; i < 2; i++) {
        input.value = 'What is ' + i + ' to the power of ' + i + '? Use LaTeX and markdown.';
        button.click();
        console.log(`Sent message ${i + 1}`);
        await sleep(1000); // Wait 1 second between messages
    }
    
    input.value = 'What is the sum from the last two answers?';
    button.click();
    console.log(`Sent final message`);
    
    console.log('Finished sending 3 messages with delays');
}

// Run the test
testRapidMessages();
```


# Testing the archive view

What to do
- Open MCP Puppeteer with window size 1920 x 1000
- Navigate to http://<addr>/?conversation_id=2025-08-19-06-57-58

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
