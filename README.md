# DummiesNmap

A dumbed-down version of the very popular Nmap tool for the people like me, who can't remember 50 BAJILLION FLAGS

## Current Features
Feature list is short but plentiful
- Base Nmap features and flags
- Guided menu and lists for categories of flags
  - Given the option to jump to different categories list below:
    - Target Specifications
    - Scan Techniques
    - Host Discovery
    - Port Specification and Scan Order
    - Service and Version Detection
    - OS Detection
    - Script Scanning (NSE)
    - Timing and Performance
    - Firewall and IDS Evasion
    - Outputs
    - Miscellaneous
- Built in history
  - Allows for user to check the following for a previous nmap run
    - Timestamp
    - Target
    - Flags used
    - Full command
  - Cross session, so you won't have to worry about it getting erased after a session has ended
    - All of the user history will be saved in a .json file in the dummiesnmap folder
    - Allows for users to use an old save and swap out the target to allow for the reuse of the command
      - For example a saved command "Nmap 192.168.256.5 -sA" can be swapped out with the new target "192.168.365.41" and the new command would be "Nmap 192.168.365.41 -sA"
- Allow for users to add in and run/save their own commands that they've used before by just inputting it
  - No need to add in "sudo nmap" as the program takes care of that
- Command clearing (a hotfix until I can solve the issue of no overwriting when you want to remove a flag or change a value)
- Fully modular code, making it more efficient and prettier on the source side
  - Also allows for an easier time to customise the code yourself if wanted
- Most importantly: Dumbed-down explanation of what each flag does so you know what it does when you choose it :D
- More to come :D

## Why this exists
The third of many random posts that track my progress as a programmer. Now a crazy but also practical and ready-made program :D

The idea of this came on a fly. I realised while running Nmap one day, that I constantly had to look back, see which flags I needed. It was very annoying, so I figured, why not make a dumbed-down version that tells you what each flag does then and there, and you can just pick and choose what you need without having to leave your terminal :D

In addition I've added a history feature, which should allow you to go back and look at all of the flag combinations you've used in the past and with which IP address/addresses. Yes I know there's the base history function with the '-oA'. '-oG', '-oN' and '-oX' flags but this skips all the hassle of having to get the file, plug it in and run. And if you still want to use it, all of Nmap's base commands are intergrated into this.

So behold the third of many repos to come about my progress and improvement. If anyone who sees this has any tips, ideas or comments, just lemme know, all feedback is much appreciated.

## How to run
```bash
git clone https://github.com/kaizokuv/dummiesnmap.git
cd dummiesnmap
python3 main.py
```

## For those of you who are lazy and willing to tweak around with aliases
Here are some aliases you guys can use for your terminal shells (bash, fish, zsh) to simplify calling the tool. 

Mind you you will still need to clone the repo first, and this is assuming you cloned the repo into your desktop and not a file. 

The alias will cd in a subshell so that once you're done using the tool, you'll go back to your original directory.

### For bash/zsh shell
```bash
alias dummiesnmap='(cd ~/dummiesnmap && python main.py)'
```
Change '~/dummiesnmap' to the desired file path if you want to set a custom file path

### For fish shell
```bash
function dummiesnmap
  pushd ~/dummiesnmap > /dev/null
  python main.py
  popd > /dev/null
end
```
Change '~/dummiesnmap' to the desired file path if you want to set a custom file path


# Thank you for using my tools :D
