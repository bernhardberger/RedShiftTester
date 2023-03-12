using StereoKit;
using System;

namespace RedShiftCalibration
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Initialize StereoKit
            SKSettings settings = new SKSettings
            {
                appName = "RedShiftCalibration",
                assetsFolder = "Assets",
            };
            if (!SK.Initialize(settings))
                Environment.Exit(1);

            // Store the initial head position for later reference
            Pose initialHeadPose = Input.Head;

            // Create assets used by the app
            Vec3 centerPosition = Input.Head.position + Input.Head.Forward * 1.5f;
            Quat centerOrientation = Quat.LookDir(-Input.Head.Forward);

            Material triangleTestImage = Material.Unlit.Copy();
            triangleTestImage[MatParamName.DiffuseTex] = Tex.FromFile("redshift_triangle.png");

            Mesh planeMesh = Mesh.GeneratePlane(new Vec2(1f, 1f), -1);
            Model planeModel = Model.FromMesh(planeMesh, triangleTestImage);

            Quat imageOrientation = Quat.FromAngles(90, 0, 0);       
            Matrix planeTransform = Matrix.TR(0, 0, -1f, imageOrientation);

            bool hasCentered = false;
           

            // Core application loop
            while (SK.Step(() =>
            {
                planeMesh.Draw(triangleTestImage, planeTransform);
                planeModel.Draw(planeTransform);

                // Create a text element
                if (!hasCentered)
                {
                    Text.Add("Press SPACE to re-center view", Matrix.TRS(Input.Head.position + Input.Head.Forward * 0.5f, Input.Head.orientation, new Vec3(-1, 1, 1)), TextStyle.Default, TextAlign.Center, TextAlign.Center);
                }

                // Center view when space key is pressed
                if (Input.Key(Key.Space).IsJustActive())
                {
                    // Compute a new pose that is centered in the user's view
                    Vec3 centerPosition = Input.Head.position + Input.Head.Forward * 1.5f;
                    Quat centerOrientation = Quat.LookDir(-Input.Head.Forward);

                    // Update the plane transform
                    planeTransform = Matrix.TR(centerPosition, centerOrientation * Quat.FromAngles(-90, 0 , 0) * Quat.FromAngles(0, 180, 0));

                    // Update the plane model
                    planeModel = Model.FromMesh(planeMesh, triangleTestImage);
                    planeModel.Draw(planeTransform);

                    hasCentered = true;

                }
            })) ;
            SK.Shutdown();
        }
    }
}
