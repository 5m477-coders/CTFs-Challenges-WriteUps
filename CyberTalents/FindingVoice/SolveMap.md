 **Finding Voice** 
 
     **1- Unzip Zip File:**
 
    `    to unzip the file we have to fix byte in the zip header.
         orginal zip header:
            00000000  50 4b 03 04 14 00 0b 00  00 00 1c a0 94 4c 8a 58  |PK...........L.X|
        after fix:
            00000000  50 4b 03 04 14 00 0b 00  08 00 1c a0 94 4c 8a 58  |PK...........L.X|
        
        now you can unzip the file with password 1234


    **WAV file **
        lets take a look at wav spectrogram using audacity 
        ![alt text]()
        
        it look like DTMF
        lets decode it using PASLE32
        and now we have the flag
        
    


