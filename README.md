# RedShiftTester

- requires .NET Framework Runtime 6.0 (https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-6.0.15-windows-x64-installer) 

Instructions:

1. Install .NET Framework 6.0 Runtime
1. Unpack the .zip file and start "RedShiftCalibration.exe"
1. put on your Varjo HMD and adjust the values for CA Correction in OpenXR Toolkit* until the image in the center looks like a flat 2D image (red and blue dots should have the same depth as the green line, it shouldn't be a 3D image). Don't worry if you won't get it 100% flat and concentrate on the center of your view.
1. remember the values you ended up with and re-enter them to any new app you launch that uses OpenXR Toolkit (you can re-use the same values you ended up with in the calibration app, but you need to re-enter them in any new app you launch, just as any other OpenXR Toolkit setting)

Tips:
- it helps to set the OpenXR Toolkit menu timeout to 3 seconds to see changes/results more quickly
- the default values (Red: +0.090, Blue: -0.022) should work for most people that have the IPD manually set in Varjo Base to their actual IPD values (measured by an optician). 
- AutoIPD is unreliable and measures different values each run and can measure different values depending if you're using lens inserts, glasses, contact lenses or just the naked eye. Set your IPD to "manual" in Varjo Base and leave it at the IPD you adjusted your CA Correction values to. The correction values are IPD dependent! If you alter your IPD you will need different values!

*needs OpenXR Toolkit >1.3.0 and only works on Varjo in Varjo Base OpenXR

### Known Issues:

#### Incompatibility of this Test-App with OpenXR Motion Compensation:
- if you're using OpenXR Motion Compensation, you will need to disable OXRMC for this app. Create the following .ini file if it doesn't already exist and set `enabled=0` in the `[startup]` section.

**%APPDATA%\\..\Local\OpenXR-MotionCompensation\RedShiftCalibration.ini:**
```ini
[startup]
enabled=0
```

---

If there are any questions, please feel free to reach out to me on discord: steiNetti#5857

---


Big thanks to @mbucchia for making the feature for correction of chromatic abberations on Varjo HMDs available in OpenXR Toolkit! (https://mbucchia.github.io/OpenXR-Toolkit/)
