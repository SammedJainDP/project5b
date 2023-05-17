# Testing Encryption/Decryption - @Sign

## Content

1. Problem statement
2. Solution approach
3. Steps to setup and run
4. Tools and technologies
5. Documentation of the related libraries
6. Use cases
7. Collaborators
8. Acknowledgement

## Problem statement

Setting up the pico_w and running the existing code on pico_w

Writing the test suite for the files aes.py and main.py

## Solution approach

UnitTest - to write test suites 

Network - to test the network connections

## Steps to setup and run
• Create an atSign and download its .atKeys file and store it locally. (Click on atSign to create one)
• Install the latest firmware.uf2 onto your Pico W from atsign-foundation/micropython Releases, as this is 
patched to enable AES CTR, which is used by atSigns.
• Connect the Pico-W to your system and put the downloaded firmware.uf2 file into the Pico-W. (Once 
you put this file into pico-w it will exit automatically)
• Clone the code from GitHub. (https://github.com/SammedJainDP/project5b.git) 
• Download Thonny IDE and place all the files of this repository in the Pico-w file system.
• Fill all the fields of the settings.json file (ssid/password of your Wi-Fi network and atSign).
• Place your .atKeys file in the ~/keys/ directory (if the folder doesn't exist, create it manually)
• Make sure pico-w is connected to internet
• Run main.py and select option 3 in the REPL ("Get privateKey for @[yourAtSign]”)
• Re-launch the REPL (run main.py again)
• Now you can select option 2 in the REPL to automatically get authenticated in your DESS (If you get 
an error when attempting to find the secondary or when trying to connect to it, run again the REPL)
• To run the aes_test_cases.py, do the following steps:
• Open the aes_test_cases.py and click on the run button on the thonny ide.
• To run the test cases for the main_test_cases.py
• Open the main_test_cases.py file in thonny 
• Click on the run button on the thonny ide.
• Thank You

## Tools and technologies

Below are the tools and technologies that we have used for this project.

[Pico_w](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

[FileZilla](https://filezilla-project.org/)

[Thonny](https://thonny.org/)

[VS Code](https://code.visualstudio.com/download)

[GitHub](https://github.com/SammedJainDP/project5b.git)

[Python](https://www.python.org/)

[micropython](https://micropython.org/)

[Atmosphere pro](https://atsign.com/resources/articles/heres-why-you-want-to-send-all-your-files-with-mospherepro/)

## Documentation of the related libraries
Below are the libraries which we have used to write the test suites.

[Unit Test](https://docs.python.org/3/library/unittest.html)

[Magicmonk](https://docs.python.org/3/library/unittest.mock.html)



## Use cases
* Used to test the existing encryption/decryption code provided by @Sign
* Helps verify the functionality of the code and reduce errors.


## Collaborators
Chandra Mouli Visweswararao

Hemanth Sai

Sammed Jain Prakash

## Acknowledgement
We thank prof. Kenneth Fletcher, Tyler and Jeremy for giving us this oppurtunity and for the support provided throughout the project phase.

