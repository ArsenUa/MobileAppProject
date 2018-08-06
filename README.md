# Simulator setup

## Setup tools
  
  1. Install Homebrew  
  `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
     or find more information [here](https://brew.sh/)
  2. Install Python 3.6+: `brew install python3`
  3. Install npm and node: `brew install npm`(`npm install -g npm`) and `brew install node` find more info about node installation [here](https://nodejs.org/en/)
  4. Install Carthage: `brew install carthage` # a simple decentralized dependency manager for Cocoa.
  5. Install libimobiledevice: `brew install libimobiledevice` # a cross platform protocol library to communicate with iOS devices.
  6. Install xcode (for ios simulator): `xcode-select --install` or [download from appstore](https://itunes.apple.com/us/app/xcode/id497799835)
  7. Install ios-deploy: `brew install ios-deploy` # install and debug iOS apps without using Xcode
  8. Install Appium: `npm install -g appium` or find more info [here](http://appium.io/)
  9. Install Appium-Python-Client: `pip install Appium-Python-Client` or find more info [here](https://github.com/appium/python-client)
  
  
## Run test:
1. Run appium server `appium` or desktop version.
2. Execute test in verbose mode `python simulatorTest.py -v`
