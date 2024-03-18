import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'dart:async';

class CaptureSequence extends StatefulWidget {
  final CameraDescription camera;
  const CaptureSequence({Key? key, required this.camera}) : super(key: key);

  @override
  _CaptureSequenceState createState() => _CaptureSequenceState();
}

class _CaptureSequenceState extends State<CaptureSequence> {
  late CameraController _controller;
  late Future<void> _initializeControllerFuture;

  @override
  void initState() {
    super.initState();
    // Initialize the controller with high image quality.
    _controller = CameraController(
      widget.camera,
      ResolutionPreset.high,
    );

    _initializeControllerFuture = _controller.initialize();
  }

  Future<void> captureImagesSequence() async {
    // Ensure the camera is initialized
    await _initializeControllerFuture;

    const int captureCount = 5; // Number of images to capture
    List<XFile> capturedImages = [];

    for (int i = 0; i < captureCount; i++) {
      try {
        // Wait for a moment before capturing the next image
        await Future.delayed(Duration(seconds: 1));

        // Attempt to capture the image
        final image = await _controller.takePicture();
        capturedImages.add(image);
        print('Image Captured: ${image.path}');

      } catch (e) {
        print(e); // Handle the error
        break; // Exit the loop if an error occurs
      }
    }

    // Process captured images, e.g., saving or displaying them
  }

  @override
  void dispose() {
    // Dispose of the controller when the widget is disposed.
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Capture Sequence')),
      // Use a FutureBuilder to display a loading spinner while waiting for the camera to initialize
      body: FutureBuilder<void>(
        future: _initializeControllerFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            // If the Future is complete, display the preview.
            return CameraPreview(_controller);
          } else {
            // Otherwise, display a loading indicator.
            return Center(child: CircularProgressIndicator());
          }
        },
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.camera),
        // Provide an onPressed callback.
        onPressed: () {
          captureImagesSequence();
        },
      ),
    );
  }
}
