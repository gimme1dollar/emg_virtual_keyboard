# Mutton
EMG Based Virtual Keyboard   
for developing Watchband-shaped IoT device input system   
  
         
## Method
```bash
(1) EMG data acquisition - OpenBCI 
(2) Pin Electrode - Self-manufactured Pin-header based Pins 
(3) Model - Convolutional Neural Network
```

## Result
* Offline Classification Training & Test    
:: Classifying 4 gestures (exploting index/middle/ring finger buttons + 1 noise) with 2-channel   
:: Validation Set Accuracy : about 99.6%   
:: Test Set Accuracy : about 85%
![다운로드](https://user-images.githubusercontent.com/20160685/88161475-fd726400-cc4a-11ea-96d2-b4463477ce35.png)

* Watchband-shaped Device Pilot Test   
:: Classifying 4 gestures with 2-channel "real-time"   
:: ( On Going, but stopped to serve military obligation (2019.4~) )     
:: ( Not very good performance, maybe by different sampling rate )   


## Publication
* 2018 학부생 연구프로그램(UGRP) 수상작 (최우수상)   
(https://www.youtube.com/watch?v=WyyjaKbNtxU)   
* Feasibility Study on Pin Electrode for sEMG_Interface.pdf   
https://drive.google.com/file/d/1wE2IgJxHEIAFnnFYu4O8L4EcwqfiJtKd/view?usp=sharing
