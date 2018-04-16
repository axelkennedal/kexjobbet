# Parameters
Number of songs from each genre: 50
Total number of songs: 300
Test/training split: 30/70
Number of MFCCS = 20
Sample rate = 44kHz

# Results
## 60s snippets
### OffsetMode START
Score: 0.975610

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            8            0            0            5            0            2
   Classical            0           11            0            1            3            0
     Hip-Hop            1            0            5            1            6            2
     Dubstep            2            1            3            7            0            2
      Reggae            2            0            1            0           12            0
        Rock            2            0            4            0            0            9


Finished classifying 90 songs.
Accuracy 57.77777777777778% [52/90]

### OffsetMode MIDDLE
Score: 0.970732

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House           11            0            1            3            0            0
   Classical            0           14            0            0            1            0
     Hip-Hop            0            0            2            1            8            4
     Dubstep            4            0            2            8            0            1
      Reggae            0            0            3            1            9            2
        Rock            1            0            2            1            0           11


Finished classifying 90 songs.
Accuracy 61.111111111111114% [55/90]

### OffsetMode END
Score: 0.946078

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            7            0            1            3            1            3
   Classical            0           14            0            0            1            0
     Hip-Hop            0            0            8            1            4            2
     Dubstep            4            0            3            5            0            3
      Reggae            2            0            5            0            6            2
        Rock            0            0            1            0            2           12


Finished classifying 90 songs.
Accuracy 57.77777777777778% [52/90]

### OffsetMode RANDOM
Score: 0.980488

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            4            0            4            4            0            3
   Classical            0           13            0            0            2            0
     Hip-Hop            1            0            6            2            3            3
     Dubstep            1            0            1            9            0            4
      Reggae            0            0            8            3            3            1
        Rock            0            0            2            0            1           12


Finished classifying 90 songs.
Accuracy 52.22222222222222% [47/90]

## 45s snippets
### OffsetMode START
Score: 0.971154

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            7            0            0            6            0            2
   Classical            0           11            0            1            3            0
     Hip-Hop            1            0            7            1            4            2
     Dubstep            2            1            2            7            1            2
      Reggae            2            0            1            0           12            0
        Rock            3            0            2            0            1            9


Finished classifying 90 songs.
Accuracy 58.888888888888886% [53/90]

### OffsetMode MIDDLE
Score: 0.961538

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            9            0            2            3            1            0
   Classical            0           14            0            0            1            0
     Hip-Hop            0            0            1            1            9            4
     Dubstep            4            0            3            6            1            1
      Reggae            0            0            1            1           10            3
        Rock            0            0            2            1            1           11


Finished classifying 90 songs.
Accuracy 56.666666666666664% [51/90]

### OffsetMode END
Score: 0.932367

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            9            0            1            0            2            3
   Classical            0           14            0            0            1            0
     Hip-Hop            2            0            7            1            4            1
     Dubstep            7            0            3            3            1            1
      Reggae            2            0            5            0            6            2
        Rock            1            0            1            0            2           11


Finished classifying 90 songs.
Accuracy 55.55555555555556% [50/90]

### OffsetMode RANDOM
Score: 0.971154

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            2            0            1            7            3            2
   Classical            0           13            1            1            0            0
     Hip-Hop            0            0            1            2            8            4
     Dubstep            2            0            4            3            1            5
      Reggae            0            0            3            2            9            1
        Rock            2            0            1            1            0           11


Finished classifying 90 songs.
Accuracy 43.333333333333336% [39/90]

## 30s snippets
### OffsetMode START
Score: 0.956731

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            5            0            0            5            3            2
   Classical            1           11            0            1            2            0
     Hip-Hop            1            0            6            3            3            2
     Dubstep            3            2            1            6            1            2
      Reggae            1            0            2            1           11            0
        Rock            2            0            2            0            1           10


Finished classifying 90 songs.
Accuracy 54.44444444444444% [49/90]

### OffsetMode MIDDLE
Score: 0.937500

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            5            0            2            6            2            0
   Classical            0           13            0            1            1            0
     Hip-Hop            0            0            1            2            8            4
     Dubstep            3            1            1            8            2            0
      Reggae            0            0            3            0            9            3
        Rock            0            0            2            0            1           12


Finished classifying 90 songs.
Accuracy 53.333333333333336% [48/90]

### OffsetMode END
Score: 0.874396

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            7            0            2            0            3            3
   Classical            0           14            1            0            0            0
     Hip-Hop            3            1            6            1            3            1
     Dubstep            5            1            3            1            2            3
      Reggae            0            0            6            0            6            3
        Rock            3            0            1            0            0           11


Finished classifying 90 songs.
Accuracy 50.0% [45/90]

### OffsetMode RANDOM
Score: 0.927885

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            4            0            1            2            4            4
   Classical            0           13            1            0            1            0
     Hip-Hop            0            0            5            1            6            3
     Dubstep            0            0            3            5            4            3
      Reggae            2            0            2            1            9            1
        Rock            3            0            1            2            0            9


Finished classifying 90 songs.
Accuracy 50.0% [45/90]

## 25s snippets
### OffsetMode START
Score: 0.937500

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            5            2            0            4            2            2
   Classical            0           11            0            2            2            0
     Hip-Hop            1            1            7            2            2            2
     Dubstep            3            4            2            4            1            1
      Reggae            1            0            2            1           11            0
        Rock            2            0            2            0            2            9


Finished classifying 90 songs.
Accuracy 52.22222222222222% [47/90]

### OffsetMode MIDDLE
Score: 0.927885

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            4            0            3            4            2            2
   Classical            0           13            0            1            1            0
     Hip-Hop            0            2            1            0            8            4
     Dubstep            1            1            1            6            4            2
      Reggae            0            0            2            1            9            3
        Rock            0            0            1            1            1           12


Finished classifying 90 songs.
Accuracy 50.0% [45/90]

### OffsetMode END
Score: 0.811594
Classifying data.
Progress: [##################################################] (90/90)
Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            8            0            3            0            1            3
   Classical            0           14            1            0            0            0
     Hip-Hop            2            1            6            1            3            2
     Dubstep            5            1            3            1            2            3
      Reggae            0            1            6            0            5            3
        Rock            4            1            0            0            0           10


Finished classifying 90 songs.
Accuracy 48.888888888888886% [44/90]

### OffsetMode RANDOM
Score: 0.908654

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            4            1            2            1            3            4
   Classical            1           12            0            0            2            0
     Hip-Hop            2            0            1            0            9            3
     Dubstep            1            2            2            2            5            3
      Reggae            0            0            1            0           13            1
        Rock            0            0            2            1            1           11


Finished classifying 90 songs.
Accuracy 47.77777777777778% [43/90]

## 20s snippets
### OffsetMode START
Score: 0.889423

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            7            3            0            2            1            2
   Classical            1           12            0            0            2            0
     Hip-Hop            1            1            5            2            4            2
     Dubstep            3            4            1            4            2            1
      Reggae            1            0            1            1           12            0
        Rock            2            0            3            0            2            8


Finished classifying 90 songs.
Accuracy 53.333333333333336% [48/90]

### OffsetMode MIDDLE
Score: 0.894231

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            4            1            1            2            3            4
   Classical            0           13            0            1            1            0
     Hip-Hop            0            2            1            0            8            4
     Dubstep            2            3            0            2            4            4
      Reggae            0            0            2            1            9            3
        Rock            0            0            1            1            1           12


Finished classifying 90 songs.
Accuracy 45.55555555555556% [41/90]

### OffsetMode END
Score: 0.787440

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            9            0            2            0            2            2
   Classical            0           14            1            0            0            0
     Hip-Hop            2            4            5            0            3            1
     Dubstep            6            3            1            1            4            0
      Reggae            0            1            7            0            4            3
        Rock            3            1            1            0            1            9


Finished classifying 90 songs.
Accuracy 46.666666666666664% [42/90]

### OffsetMode RANDOM
Score: 0.894231
Classifying data.
Progress: [##################################################] (90/90)
Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            1            0            4            2            4            4
   Classical            1           12            2            0            0            0
     Hip-Hop            1            0            3            0            8            3
     Dubstep            0            1            6            1            1            6
      Reggae            1            0            2            0            9            3
        Rock            3            0            1            0            1           10


Finished classifying 90 songs.
Accuracy 40.0% [36/90]

## 15s snippets
### OffsetMode START
Score: 0.841346

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            6            5            0            1            2            1
   Classical            2           11            0            0            2            0
     Hip-Hop            2            2            5            0            4            2
     Dubstep            2            4            0            4            5            0
      Reggae            2            0            0            1           12            0
        Rock            2            0            1            0            4            8


Finished classifying 90 songs.
Accuracy 51.111111111111114% [46/90]

### OffsetMode MIDDLE
Score: 0.875000

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            4            1            1            1            4            4
   Classical            0           13            0            1            1            0
     Hip-Hop            0            2            0            1            8            4
     Dubstep            1            4            1            3            2            4
      Reggae            1            0            3            1            7            3
        Rock            1            0            0            2            0           12


Finished classifying 90 songs.
Accuracy 43.333333333333336% [39/90]

### OffsetMode END
Score: 0.666667

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            9            1            4            0            1            0
   Classical            0           12            3            0            0            0
     Hip-Hop            0            5            6            0            2            2
     Dubstep            6            4            1            1            2            1
      Reggae            0            3            8            0            3            1
        Rock            2            1            1            0            4            7


Finished classifying 90 songs.
Accuracy 42.22222222222222% [38/90]

### OffsetMode RANDOM
Score: 0.884615

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            0            2            5            1            2            5
   Classical            0           13            1            0            1            0
     Hip-Hop            0            0            6            0            6            3
     Dubstep            2            2            5            3            0            3
      Reggae            1            0            4            0            8            2
        Rock            1            0            2            0            0           12


Finished classifying 90 songs.
Accuracy 46.666666666666664% [42/90]

## 10s snippets
### OffsetMode START
Score: 0.769231

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            6            6            0            0            2            1
   Classical            1           11            0            1            2            0
     Hip-Hop            1            7            2            0            3            2
     Dubstep            1            7            1            2            4            0
      Reggae            1            1            1            0           12            0
        Rock            2            0            1            0            4            8


Finished classifying 90 songs.
Accuracy 45.55555555555556% [41/90]

### OffsetMode MIDDLE
Score: 0.846154

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            2            1            0            1            6            5
   Classical            0           12            0            2            1            0
     Hip-Hop            1            2            1            0            7            4
     Dubstep            3            3            0            0            4            5
      Reggae            0            0            3            2            7            3
        Rock            0            0            2            0            0           13


Finished classifying 90 songs.
Accuracy 38.888888888888886% [35/90]

### OffsetMode END
Score: 0.579710

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            5            2            4            0            1            3
   Classical            0           10            4            1            0            0
     Hip-Hop            0           10            1            0            2            2
     Dubstep            7            3            1            1            3            0
      Reggae            1            5            3            1            4            1
        Rock            3            2            0            0            4            6


Finished classifying 90 songs.
Accuracy 30.0% [27/90]

### OffsetMode RANDOM
Score: 0.836538

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            2            1            5            1            2            4
   Classical            0           13            1            1            0            0
     Hip-Hop            0            0            7            0            6            2
     Dubstep            2            3            6            0            1            3
      Reggae            0            0            5            0            9            1
        Rock            0            1            2            0            0           12


Finished classifying 90 songs.
Accuracy 47.77777777777778% [43/90]

## 5s snippets
### OffsetMode START
Score: 0.701923

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            5            7            0            1            2            0
   Classical            0           12            0            1            2            0
     Hip-Hop            0            6            1            2            3            3
     Dubstep            4            5            1            3            1            1
      Reggae            1            1            1            0           10            2
        Rock            0            2            0            1            4            8


Finished classifying 90 songs.
Accuracy 43.333333333333336% [39/90]

### OffsetMode MIDDLE
Score: 0.836538

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            2            1            0            2            6            4
   Classical            0           11            0            3            1            0
     Hip-Hop            1            2            1            0            8            3
     Dubstep            2            3            0            1            5            4
      Reggae            1            0            3            1            8            2
        Rock            0            0            0            2            1           12


Finished classifying 90 songs.
Accuracy 38.888888888888886% [35/90]

### OffsetMode END
Score: 0.396135

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            0            9            1            0            3            2
   Classical            0           13            0            0            0            2
     Hip-Hop            0           14            0            0            1            0
     Dubstep            0            7            2            1            2            3
      Reggae            1           11            1            0            0            2
        Rock            3            5            1            0            0            6


Finished classifying 90 songs.
Accuracy 22.22222222222222% [20/90]

### OffsetMode RANDOM
Score: 0.841346

Confusion matrix:

                     House     Classical       Hip-Hop       Dubstep        Reggae          Rock
       House            5            0            5            0            4            1
   Classical            0           13            0            1            1            0
     Hip-Hop            1            1            2            0           10            1
     Dubstep            4            2            3            0            4            2
      Reggae            2            0            2            0           11            0
        Rock            9            0            3            0            1            2


Finished classifying 90 songs.
Accuracy 36.666666666666664% [33/90]
