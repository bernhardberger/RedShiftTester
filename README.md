# RedShiftTester

- requires .NET Framework Runtime 6.0 (https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-6.0.15-windows-x64-installer) 

Instructions:

1. Install .NET Framework 6.0 Runtime
1. Unpack the .zip file and start "RedShiftCalibration.exe"
1. put on your Varjo HMD and adjust the values for CA Correction in OpenXR Toolkit* until the image in the center looks like a 2D image (red and blue dots should have the same depth as the green line, it shouldn't be a 3D image)
1. remember the values you ended up with and re-enter them to any new app you launch that uses OpenXR Toolkit (you can re-use the same values you ended up with in the calibration app, but you need to re-enter them in any new app you launch, just as any other OpenXR Toolkit setting)

Tips:
- it helps to set the OpenXR Toolkit menu timeout to 3 seconds to see changes/results more quickly
- the default values (Red: +0.090, Blue: -0.022) should work for most people that have the IPD manually set in Varjo Base to their actual IPD values (measured by an optician). 
- AutoIPD is unreliable and measures different values each run. Set your IPD to "manual" in Varjo Base and leave it at the IPD you adjusted your CA Correction values to. The correction values are IPD dependent! If you alter your IPD you will need different values!

*needs OpenXR Toolkit > 1.3.0 and only works on Varjo in Varjo Base OpenXR