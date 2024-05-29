# Faster Lock on SANS Holiday Hack

1. refer to video: https://www.youtube.com/watch?v=27rE5ZvWLU0 

# Or.... do it the hacker way..😎
1. Right click - Inspect element on the iframe of the lock. To open up the developer tools
    - In the Elements Tab, Find the `<script> { the game code logic is in here } </script>` copy the script
    - I recommend copy and pasting the javascript code into Notepad++ and inspect the code
2. You will notice some interesting (global) variables and functions
  ```
  GenerateCombination()
  lock_numbers
  moveLockIntoUnlockedPosition()
  ```

3. In the Console Tab of the Chrome developer tools, paste in any of the variable names or function names, press enter. 
4. OPEN SESAME! YOU'RE DONE!