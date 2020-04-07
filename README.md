# CaptureTheCat
Jogo onde há um gato e um tabuleiro, em uma parte o gato precisa sair do tabuleiro, na outra o tabuleiro precisa capturar o gato.

Executar o arquivo com extensão .bat para rodar

This is a project made for "Resoluçao de Problemas" class, it is a game by now diveded on 2 stages

**1st - You are the cat and need to scape from the mat**\
**2nd - You are the mat and your mission is capture another cat**\

**My Resolutions**
 - Used Dijkstra's algorithm, so the cat always run to the closest exit.
 - To the 2nd I have used the same algorithm so the mat will always try to block the closest exit for the cat.
 

**_Some game informations:_**
 - The table consists of a grid / matrix 11x11
 - This table contens some BLOCKED places where the cat can`t go
 - This table also contains EXITS where the cat can escape and WIN

**To the 1st case - You're the Cat:**\
    **_You will lose the game if:_**\
        - Your cat goes out of the table range
        - Your cat will go some blocked place\
    **_You will WIN the game when:_**\
        - You cat arive some exit
    _You are aware of the number of steps you need to reach the closest exit:_\
        - Your score is based on how far you are from the ideal number of steps.  

**To the 2nd case - You're the Table**\
    **_You will Lose the game if:_**\
        - The cat can reach some of the exits\
        - You don't make a move  
    **_You wil WIN the game when:_**\
     - The cat can't reach any exit

