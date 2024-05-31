## Na'an Shfity's Card Game


1. Get JS
2. Interesting code pieces
    - Notice the isValid() function
    - ajax POST method request data for score comparison
    - notice the ajax POST request
    ```
            complete: function (data) {
            var response = JSON5.parse(data.responseText)
            console.log(response)
            if (response.request == true) {
                if (response.data.conduit) {
                    __POST_RESULTS__(response.data.conduit)
                }
                ShiftyElfScoreToast.setText("Shifty's Score: " + response.data.shifty_score)
                PlayerScoreToast.setText("Player's Score: 8") // <----- Look here 
                win_lose_score_message(response.data.score_message, response.data.win_lose_tie_na, response.data)
            } else if (response.data) {
                Talk(response.data)
            }
        }
    ```
3. Can use burp suite to modify the HTTP POST request player score or the card to NaN
4. need to win at least once. 
5. Chrome Developer tools can modify the JS or HTTP request and repeat the winning NaN hand.  